from modules.database.Mysql4 import Mysql4

import pandas as pd

from tqdm import tqdm
import pprint


if __name__ == '__main__':
    mysql = Mysql4(host='172.31.19.191', db_name='orix_data', user='root')

    # =======================================================
    # Q.1
    sql = "2018年1月21日 被験者No3のデータを取得せよ．\
        取得項目は日付，速度，経度，緯度"
    #data = mysql.excute_fetch(sql)
    #print(data)
    #pprint.pprint(data)
    
    

    