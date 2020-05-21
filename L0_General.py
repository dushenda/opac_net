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
import baseClass


class GenePara:
    db = baseClass.SqlInfo(db_name='General')

    def tosql_ATR_cali(self, df):
        '''

        :param df:pandas DataFrame
        :return:
        '''
        db_engine = create_engine(self.db.engine_all_para)
        print(self.db)
        table_name = "222"
        df.to_sql(name=table_name, con=db_engine, if_exists="replace", index=False)

    def tosql_ATR_cali_from_csv(self, path):
        df = pd.read_csv(path)
        band_num = range(1,9)
        df.insert(loc=0, column="band_num", value=band_num)
        self.tosql_ATR_cali(df)
        print(df)


def main():
    g = GenePara()
    path = "./example/cali_factor/ATR2019.csv"
    g.tosql_ATR_cali_from_csv(path)


if __name__ == '__main__':
    main()
