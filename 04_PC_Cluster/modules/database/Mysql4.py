# database
#from sqlalchemy import create_engine
import pymysql.cursors
import mysql.connector
#import sqlite3

import numpy as np

import pandas as pd

from tqdm import tqdm

class Mysql4:
    def __init__(self, host='172.31.19.191', db_name='orix_data', user='root'):
        self.con = mysql.connector.connect(
        host=host,
        db=db_name,
        user=user,
        passwd='0gur11a6'
        )
        self.cur = self.con.cursor(dictionary=True)

    def excute_fetch(self, sql):
        self.cur.execute(sql)
        rows = self.cur.fetchall()
        return rows

    def regist(self, sql):
        self.cur.execute(sql)
        self.con.commit()

    def mysql_close(self):
        self.con.close()

    def dict2df(self, data):
        df = pd.DataFrame([], columns=data[0].keys())

        for i in tqdm(range(len(data))):
            df1 = pd.DataFrame([data[i].values()], columns=data[i].keys())
            df = pd.concat([df, df1])

        df.reset_index(inplace=True, drop=True)

        return df

if __name__ == '__main__':

    mysql = Mysql4(host='172.31.19.191', db_name='orix_data', user='root')
    mysql.create_normal_list(mysql)

    limit_velocity_list = mysql.sql_excute_fetch('SELECT * FROM `limit_velocity` WHERE sub = 1')


