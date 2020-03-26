from modules.database.Mysql4 import Mysql4

import pandas as pd

from tqdm import tqdm
import pprint

# 描画関係
import matplotlib as mpl
import matplotlib.pyplot as plt

# 地図関係
import folium
from folium import plugins

if __name__ == '__main__':
    mysql = Mysql4(host='172.31.19.191', db_name='orix_data', user='root')

    # =======================================================
    # Q.1
    sql = "2018年1月21日 被験者No3のデータを取得せよ．\
        取得項目は日付，速度，経度，緯度"
    data = mysql.excute_fetch(sql)
    #print(data)
    #pprint.pprint(data)
    pprint.pprint(data)


    # =======================================================
    # Q.2
    #取得した dict型をpandas形式に変換するプログラムを作成せよ


    # =======================================================
    # Q.3
    #取得した pandas型データを地図上にプロットするプログラムを作成せよ
    # ヒント：foliumを使用します
    