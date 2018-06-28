# -*- coding:utf-8 -*-

from sqlalchemy import create_engine


def df_to_mysql(df, table_name):
    connect = create_engine('mysql+pymysql://root:root@localhost:3306/premetheus?charset=utf8')
    df.to_sql(name=table_name, con=connect, if_exists='replace')

    print('insert end')
