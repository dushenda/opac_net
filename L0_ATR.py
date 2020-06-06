#!/usr/bin/env python
# -*- encoding: utf-8 -*-

"""
@ide        : PyCharm
@project    : FTPTest
@file       : L0_ATR.py
@author     : CALIBRATION
@time       : 2020/5/9 20:32
@description: None
"""
import ftplib
import datetime
import os
import pandas as pd
from sqlalchemy import create_engine
import re

import baseclass


def trans_time(df_s_ele, date_str):
    # 联合df['时间']=时间和文件名date_str为日期的函数，用于pandas转换
    # df_s_ele = df['测量时间'][i],date_str = table_name
    # 传输series time，输出联合datetime
    try:
        dt_date = datetime.datetime.strptime(date_str, "%Y%m%d")
        dt_time = datetime.datetime.strptime(df_s_ele, "%H:%M")
        res = datetime.datetime.combine(dt_date.date(), dt_time.time())
        return res
    except ValueError:
        return pd.NaT


class DNATR:
    today_ftp_file = ''
    today_local_file = ''
    today_local_file_abs = ''

    ftp_path = ''
    local_path = ''
    # 仪器编号str
    ins_num = ''

    def __init__(self, ins_num='01', local_path='/test_data/'):
        # ins_num为仪器编号
        self.ftp = baseclass.FtpInfo()
        self.db = baseclass.SqlInfo()
        self.set_ins_num(ins_num)
        self.set_path(local_path)
        self.set_file_name()

    # 保存至MySQL，分为强制更新和比较更新两种force&cmp，使用函数为save_mysql_all
    def save_all_mysql_force(self):
        """
        强制更新将所有的文件下载并且保存至mysql
        :return:
        """
        self.save_all_mysql("replace")

    def save_all_mysql_cmp(self):
        """
        比较更新文件
        :return:
        """
        self.save_all_mysql("fail")

    def save_all_mysql(self, option):
        """
        更新FTP到MySQL
        :param option: 更新方式见pandas的to_sql方法
        :return:
        """
        db_engine = create_engine(self.db.engine_all_para)
        # 查询得到所有表格，并且加上文件后缀.csv
        q = db_engine.execute('SHOW TABLES')
        q_res = q.fetchall()
        tables = [x[0] + '.csv' for x in q_res]
        # 比较文件，获取本地文件目录，得到服务器未上传表格
        file_names = list(filter(lambda x: re.match('.*.csv', x) is not None, os.listdir(self.local_path)))
        need_to_add_files = set(file_names) - set(tables)
        for file_name in need_to_add_files:
            # 将未写入的表格写入服务器
            table_name = os.path.splitext(file_name)[0]
            file_abs_path = self.local_path + file_name
            df = pd.read_csv(file_abs_path, encoding='gbk')
            df['测量时间'] = df['测量时间'].apply(trans_time, args=(table_name.split('_')[-1],))
            df.to_sql(name=table_name, con=db_engine, if_exists=option)

    def save_today_mysql(self):
        """
        将今天的文件下载并且保存至mysql
        :return:
        """
        db_engine = create_engine(self.db.engine_all_para)
        # 取得table_name = DN_ATR01_20200510这样的结果
        file_name = os.path.basename(self.today_local_file_abs)
        table_name = os.path.splitext(file_name)[0]
        # 整理df格式
        df = pd.read_csv(self.today_local_file_abs, encoding='gbk')
        df['测量时间'] = df['测量时间'].apply(trans_time, args=(table_name.split('_')[-1],))
        df.to_sql(name=table_name, con=db_engine, if_exists="replace")

    def get_all_file(self):
        """
        比较本地的文件名，从FTP上同步文件
        :return:None
        """
        with ftplib.FTP(host=self.ftp.ftp_host, user=self.ftp.ftp_usr, passwd=self.ftp.ftp_psd) as ftp:
            ftp_file_list = map(lambda x: self.get_local_file_name(x), ftp.nlst(self.ftp_path))
            ftp_file_set = set(ftp_file_list)
            local_file_list = set(filter(lambda x: re.match('.*.csv', x) is not None, os.listdir(self.local_path)))
            dwn_file_set = ftp_file_set - local_file_list
            for local_file_name in dwn_file_set:  # DN_ATR01_20200510.csv这样的结果
                ftp_file_name = local_file_name.split('_')[-1]
                self.get_file_from_ftp(self.ftp_path, ftp_file_name, self.local_path, local_file_name)
                print("get{}".format(local_file_name))  # 获取的文件

    def get_today_file_from_01(self):
        """
        下载当日的文件
        :return: None，成功会产生新文件
        """
        self.get_file_from_ftp(self.ftp_path, self.today_ftp_file, self.local_path, self.today_local_file)

    def get_file_from_ftp(self, path_ftp, file_ftp, path_local, file_local):
        """
        下载文件
        :param path_ftp: ftp服务器上面的文件目录
        :param file_ftp: ftp服务器上的文件名称
        :param path_local: 保存至本地的路径,末尾要加上/，如usr/，如下载当前目录,则输入为''
        :param file_local: 保存至本地的文件名称
        :return:None，下载文件到本地,ftp到local
        """
        new_local_file = path_local + file_local
        with ftplib.FTP(host=self.ftp.ftp_host, user=self.ftp.ftp_usr, passwd=self.ftp.ftp_psd) as ftp:
            try:
                ftp.cwd(path_ftp)
                buf_size = 1024
                filename_ftp = file_ftp
                with open(new_local_file, "wb") as file_handle:
                    ftp.retrbinary('RETR %s' % filename_ftp, file_handle.write, buf_size)  # 接收服务器上文件并写入本地文件
            except ftplib.all_errors:
                if os.path.exists(new_local_file):
                    os.remove(new_local_file)

    def get_local_file_name(self, ftp_file_name):
        local_file_name = 'DN_ATR{}_{}'.format(self.ins_num, ftp_file_name)
        return local_file_name

    def set_ins_num(self, ins_num):
        self.ins_num = ins_num

    def set_path(self, local_path):
        self.local_path = local_path
        self.ftp_path = "ATR{}/".format(self.ins_num)

    def set_file_name(self):
        time_str = datetime.datetime.now().strftime("%Y%m%d")
        self.today_ftp_file = time_str + '.csv'
        self.today_local_file = 'DN_ATR' + self.ins_num + '_' + time_str + '.csv'
        self.today_local_file_abs = self.local_path + self.today_local_file


def main():
    # unit test
    dn_atr = DNATR()
    # dn_atr.get_all_file()
    # dn_atr.save_all_mysql()
    dn_atr.get_today_file_from_01()
    dn_atr.save_today_mysql()
    # pass


if __name__ == '__main__':
    main()
