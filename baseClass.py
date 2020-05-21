#!/usr/bin/env python
# -*- encoding: utf-8 -*-

"""
@ide        : PyCharm
@project    : FTPTest
@file       : baseClass.py
@author     : CALIBRATION
@time       : 2020/5/20 18:03
@description: None
"""


class FtpInfo:
    ftp_host = ''
    ftp_usr = ''
    ftp_psd = ''

    def __init__(self):
        self.set_ftp_profile()

    def __str__(self):
        return "ftp_host:{0}\nftp_usr:{1}\nftp_psd:{2}".format(self.ftp_host, self.ftp_usr, self.ftp_psd)

    def set_ftp_profile(self, host='202.127.202.6', usr='RADCALNET', psd='1Q2W3E4R'):
        """
        设置ftp服务器登录参数
        :param host:数据库地址，输入服务器所在公网地址即可
        :param usr:用户
        :param psd:密码
        :return:
        """
        self.ftp_host = host
        self.ftp_usr = usr
        self.ftp_psd = psd


class SqlInfo:
    db_driver = ""
    db_usr = ""
    db_psd = ""
    db_host = ""
    db_port = ""
    db_name = ""
    engine_all_para = ""

    def __init__(self, db_driver='mysql+mysqlconnector', db_usr='root', db_psd='1q2w3e4r', db_host='118.31.70.60',
                 db_port='3306',
                 db_name='Level0'):
        self.db_driver = db_driver
        self.db_usr = db_usr
        self.db_psd = db_psd
        self.db_host = db_host
        self.db_port = db_port
        self.db_name = db_name
        self.engine_all_para = db_driver + '://' + db_usr + ':' + db_psd + '@' + db_host + ':' + db_port + '/' + db_name

    def __str__(self):
        return "class_name:{0}\ndb_driver={1}\ndb_usr={2}\ndb_psd={3}\ndb_host={4}\ndb_port= {5}\ndb_name= {6}".format(
            "sqlinfo", self.db_usr, self.db_psd, self.db_host, self.db_port, self.db_name, self.engine_all_para)


def main():
    f = FtpInfo()
    print(f)
    s = SqlInfo()
    print(s)


if __name__ == '__main__':
    main()
