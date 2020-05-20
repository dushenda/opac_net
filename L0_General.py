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





class GenePara:
    def tosql_ATR_cali(self, ATR_cali):
        '''

        :param ATR_cali: 字典，输入ATR仪器的定标系数，按月为单位
        :return:
        '''
        db_engine = create_engine(self.engine_all_para)

    def tosql_ATR_cali_from_csv(self, path):
        df = pd.read_csv(path)


def main():
    a = SqlInfo()
    print(a)


if __name__ == '__main__':
    main()
