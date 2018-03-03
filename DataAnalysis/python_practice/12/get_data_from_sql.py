# -*- coding: utf-8 -*-
import pymysql
import pandas as pd
from sqlalchemy import create_engine

"""


conn = pymysql.connect(host='localhost', user='root', password='root', database='test', port=3306, charset='utf8')
select_sql = "SELECT * FROM all_gzdata"
data1 = pd.read_sql(select_sql, conn)
print(data1.head())

"""

connect = create_engine('mysql+pymysql://root:root@localhost:3306/test?charset=utf8')
sql = pd.read_sql('all_gzdata', connect, chunksize=10)
print([i for i in sql])
