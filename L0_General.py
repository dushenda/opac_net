#!/usr/bin/env python
# -*- encoding: utf-8 -*-

"""
@ide        : PyCharm
@project    : FTPTest
@file       : L0_General.py
@author     : CALIBRATION
@time       : 2020/5/13 13:41
@description: 用来上传Calibration
                    ATR_Cal.csv	ATR定标系数
                    PSR _Cal.csv	PSR定标系数
                    Net_Cal.csv	气溶胶、水汽定标系数、臭氧吸收系数
                    BRDF	BRDF model.csv	BRDF模型参数
                    Reference	ρReference.csv	参考光谱
                    ATR_RSR.csv	ATR通道响应
                    ATR_RSR_25.csv	2.5nm通道响应
"""

from sqlalchemy import create_engine
import pandas as pd

import baseclass
import basefun


class GenePara:
    db = baseclass.SqlInfo(db_name='General')

    def __str__(self):
        return "class General\ncali(ATR,PSR),BRDF,Ref,RSR set&get"

    def tosql_cali(self, df, table_name):
        """

        :param df: pandas DataFrame
        :param table_name:to sql table name
        :return:
        """
        db_engine = create_engine(self.db.engine_all_para)
        df.to_sql(name=table_name, con=db_engine, if_exists="replace", index=False)

    def tosql_Ins_cali_from_csv(self, path, table_name):
        """
        ATR、PSR定标系数写入数据库
        :param path: file path
        :param table_name: sql table name
        :return:
        """
        df = pd.read_csv(path)
        band_num = range(1, 9)
        df.insert(loc=0, column="band_num", value=band_num)
        self.tosql_cali(df, table_name)

    def tosql_BRDF_from_csv(self, path, table_name):
        df = pd.read_csv(path)
        self.tosql_cali(df, table_name)

    def tosql_Ref_from_csv(self, path):
        table_name = "ReferenceReflectance"
        df = pd.read_csv(path)
        self.tosql_cali(df, table_name)

    def tosql_RSR_from_csv(self, path, table_name):
        df = pd.read_csv(path)
        self.tosql_cali(df, table_name)



def main():
    g = GenePara()
    print(g)
    # read RSR to db
    # import os
    # path = "./example/RSR/"
    # path_list = os.listdir(path)
    # for filename in path_list:
    #     table_name = filename.split(".")[0]
    #     g.tosql_RSR_from_csv(path+filename, table_name)


if __name__ == '__main__':
    main()
