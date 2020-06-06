#!/usr/bin/env python
# -*- encoding: utf-8 -*-

"""
@ide        : PyCharm
@project    : FTPTest
@file       : L1_Ground.py
@author     : CALIBRATION
@time       : 2020/5/25 14:51
@description: None
"""
import pandas as pd
import baseclass
from sqlalchemy import create_engine


class RadATR:
    def __init__(self):
        self.db = baseclass.SqlInfo(db_name="Level0")
        self.ftp = baseclass.FtpInfo()

    def cal_rad(self, tb_dn, tb_fac):
        engin = create_engine(self.db.engine_all_para)
        df_dn = pd.read_sql_table(tb_dn, engin)
        self.db.set_para(db_name="General")
        engin2 = create_engine(self.db.engine_all_para)
        df_fac = pd.read_sql_table(tb_fac, engin2)
        print(df_dn)
        print(df_fac)

    def save_to_mysql(self):
        pass


class RadNet:
    pass


def main():
    a = RadATR()
    a.cal_rad("DN_ATR01_20200101", "ATR_Cali_Fac_2019_All")


if __name__ == '__main__':
    main()
