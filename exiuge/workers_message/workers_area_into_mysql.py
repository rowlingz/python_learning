# -*- coding:utf-8 -*-

import pandas as pd
import re
import pymysql


def re_split(string):
    """字符串分割成列表"""
    pattern = r"[,/ （）、，。./()]"
    result = re.split(pattern, string.strip())
    return [i for i in result if i]


def sql_insert(area):
    """生成【插入】语句"""
    province, county, id = area[0], area[1], area[2]

    sql_insert_worker_area = "INSERT INTO workers_area (area_id, workers_id) " \
                             "(SELECT area.id, workers.id FROM area, workers " \
                             "WHERE area.province LIKE '%s' AND area.county LIKE '%s' " \
                             "AND workers.id = %s)" % ('%' + province + '%', '%' + county + '%', id)

    return sql_insert_worker_area


def sql_check(area):
    """生成 【查询】语句"""
    province, county, id = area[0], area[1], area[2]
    sql_check_worker_area = "SELECT * FROM area, workers, workers_area " \
                            "WHERE area.id = workers_area.area_id AND " \
                            "area.province LIKE '%s' AND area.county LIKE '%s' " \
                            "AND workers_area.workers_id = %s" % ('%' + province + '%', '%' + county + '%', id)

    return sql_check_worker_area


class Inventory_data:
    def __init__(self):
        conn = pymysql.connect(host="127.0.0.1",
                               user="root",
                               password="root",
                               database="premetheus",
                               port=3306,
                               charset='utf8')
        self.conn = conn

    def insert_message(self, area_data):
        # 对含地区的df含 (province, city, county, workers_id)进行逐行分析
        error = []
        for i in range(len(area_data)):
            area_split = re_split(str(area_data.iloc[i, 3]))
            province = str(area_data.iloc[i, 1]).strip()
            id = int(area_data.iloc[i, 0])
            for county in area_split:
                # print(area_split)
                area = [province, county.strip(), id]
                insert_sql = sql_insert(area)
                check_sql = sql_check(area)
                conn = self.conn
                cur = conn.cursor()

                try:
                    cur.execute(check_sql)
                    if cur.rowcount != 0:
                        continue
                    else:
                        cur.execute(insert_sql)
                        if cur.rowcount == 0:
                            error.append([id, province, county])
                        else:
                            conn.commit()
                except Exception as e:
                    print("insert error" + str(e))
                finally:
                    cur.close()

        self.conn.close()
        return error

    def updet_message(self, area_data):
        # 更新workers_area中的地区新区
        pass


if __name__ == "__main__":

    file_name = '输入数据.xlsx'

    area_data = pd.read_excel(file_name, sheet_name='Sheet3', usecols=[0, 1, 2, 3], encoding='utf-8')

    inventory_data = Inventory_data()
    error = inventory_data.insert_message(area_data)

    f = open('lose_area.txt', 'w', encoding='utf-8')
    f.write(str(error))

    print(error)
    print(len(error))
    print('end')



