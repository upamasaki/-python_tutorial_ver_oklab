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

    sql = "SELECT `DATE`, `velocity_kmh`,`longitude`, `latitude` FROM `Drive_recorder` WHERE `sub`=3 AND DATE_FORMAT(`DATE`, '%Y%m%d')=20180121"
    data = mysql.excute_fetch(sql)
    #print(data)
    #pprint.pprint(data)

    pprint.pprint(data[0])

    df = mysql.dict2df(data)
    print(df)

    ####################################
    # map init
    LAT = df.latitude.iloc[0]
    LNG = df.longitude.iloc[0]
    m = folium.Map(location=[LAT, LNG])

    # mapping
    for i in range(len(df)):
        folium.Marker(location = [df.latitude.iloc[i], df.longitude.iloc[i]], popup = "DATE:{}".format(df.DATE.iloc[i])).add_to(m)

    # save
    m.save("./output/Map.html")