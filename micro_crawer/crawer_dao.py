# -*- coding:utf-8 -*-
import pymysql
db = pymysql.connect(host = '192.168.1.105', database = 'crawer',password = 'root', user = 'root', charset = 'utf8')
cursor = db.cursor()

class position_dao :
    def insert_position(self, postion) :
        try :  
            # INSERT INTO position_info VALUES(1, "北京", "Python开发",20.5,"机器学习", "这真是一个好工作啊");
            insert_sql = 'INSERT INTO position_info(city, position_name, salary, type, detail_info) VALUES(%s,%s,%s,%s,%s)'
            cursor.execute(insert_sql, (postion['city'], postion['position_name'], postion['salary'], postion['type'], postion['detail_info']))
            db.commit()
        except Exception as err :
            print(err)
            print('sql error')
            return False
        return True