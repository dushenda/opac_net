# opac_net

[![](https://img.shields.io/badge/sponsor-KLOCC-red)](http://klocc.aiofm.ac.cn/sysjj/sysjj/)
![](https://img.shields.io/badge/team-software-brightgreen)

what：自动化定标系统

how：
- C++处理数据的部分
- Python完成网络编程部分（爬虫和数据同步）
- 使用Python SQL Alchemy + MySQL完成数据库
- 使用C++ Qt GUI QtQuick完成客户端软件编写
- 使用SWIG嵌入脚本（+）
- web显示数据（+）
- 移动端Kotlin Android开发（+）

why：自动化处理定标数据，使得仪器数据处理的高效，可靠，实时性强

## section

### Level0

Level0为数据获取、读取、设置部分，Python实现

1. [L0_General](./doc/L0_General.md)，获取一般数据，仪器定标系数
2. [L0_ATR](./doc/L0_ATR.md)，获取ATR仪器的DN值
3. [L0_HIM](./doc/L0_HIM.md)，获取HIM仪器的DN值
4. [L0_PSR](./doc/L0_PSR.md)，获取PSR仪器的DN值
5. [L0_Net](./doc/L0_Net.md)，获取网络下载数据，影像的DN值，定标系数，臭氧，水汽值
6. [L0_Ref](./doc/L0_Ref.md)，获取连续光谱曲线

## Level1

Level1为数据的第一步处理过程，C++11实现