# -*- coding:utf-8 -*-

# 查询信息：
import pymysql
import pandas as pd


def convice_dic_sql(dictory, table_name):
    sql_con = []
    sql_val = []
    for key in dictory.keys():
        condition = table_name[0] + '.' + key + ' LIKE %s '
        value = '%' + dictory[key] + '%'
        sql_con.append(condition)
        sql_val.append(value)

    string = 'AND '.join(sql_con)

    return string, sql_val


def worker_from_area(string):
    # 查询（目标地区）---（师傅信息）
    """ string = "a.province like '%北京%'" """

    sql_select = "SELECT w.id, w.姓名, w.电话, a.province, a.city, a.county " \
                 "FROM workers AS w, area AS a, workers_area AS wa " \
                 "WHERE wa.area_id=a.id AND wa.workers_id=w.id AND %s GROUP BY w.id" % string

    return sql_select


def worker_from_service(string):
    # 查询（目标服务）---（师傅信息）
    """  string1 = 's.主类别 LIKE '%家庭维修%'' """
    sql_select = "SELECT w.id, w.姓名, w.电话, s.主类别, s.类目, s.详情 " \
                 "FROM workers AS w, service AS s, workers_service AS ws " \
                 "WHERE w.id=ws.workers_id AND s.id=ws.service_id AND %s GROUP BY w.id GROUP BY w.id" % string

    return sql_select


def area_from_workers_name(name):
    # 查询（目标师傅名字）--（基本信息--姓名/城市）
    """根据师傅名字查询   string = '陈海云'   """

    sql = "SELECT w.id, w.姓名, w.电话, a.province, a.city, a.county " \
          "FROM workers AS w, area AS a, workers_area AS wa " \
          "WHERE w.姓名='%s' AND a.id =wa.area_id AND w.id=wa.workers_id GROUP BY a.id" % name

    return sql


def service_from_workers_name(name):
    # 查询（目标师傅名字）--（基本服务）
    """根据师傅名字查询   string = '陈海云'   """

    sql = "SELECT w.id, w.姓名, w.电话, s.详情 " \
          "FROM workers AS w, service AS s, workers_service AS ws " \
          "WHERE w.姓名='%s' AND s.id=ws.service_id AND w.id=ws.workers_id GROUP BY s.id" % name

    return sql


def worker_all_message_from_name(name):
    # 根据名字  --查询师傅的所有信息

    sql = "SELECT w.id, w.姓名, w.电话, s.详情, a.province, a.city, a.county " \
          "FROM workers AS w, workers_area AS wa, workers_service AS ws, area AS a, service AS s " \
          "WHERE wa.workers_id=w.id AND ws.workers_id=w.id AND a.id=wa.area_id " \
          "AND s.id=ws.service_id AND w.姓名='%s' " % name

    return sql


def match_workers_from_service_area(area, service):
    #    area = "a.province LIKE '%北京%'"  service = "s.`主类别` LIKE '%家庭维修%'"
    """查询指定地区/类别 合适的师傅"""

    sql = "SELECT w.id, w.姓名, w.电话, a.province, a.city, a.county, s.详情 " \
          "FROM workers AS w, workers_area AS wa, workers_service AS ws, area AS a, service AS s " \
          "WHERE s.id=ws.service_id AND a.id=wa.area_id AND w.id=wa.workers_id AND w.id=wa.workers_id " \
          "AND %s AND %s GROUP BY w.id" % (area, service)

    return sql


def get_data(sql):
    conn = pymysql.connect(host="127.0.0.1",
                           user="root",
                           password="root",
                           database="premetheus",
                           port=3306,
                           charset='utf8')
    cur = conn.cursor()
    cur.execute(sql)
    if cur.rowcount == 0:
        print("匹配失败")
    else:
        result = cur.fetchall()
        print(pd.DataFrame(list(list(i) for i in result)))

    cur.close()
    print('end')
    conn.close()


string = 'a.county="%s"' % '东城区'
string = 'a.province="%s"' % '北京市'

# string1 = 's.主类别="%s"' % '家庭维修'
#
# string = 'wa.workers_id=%d' % 1


area = "a.province='%s'" % '北京市'
service = "s.`主类别`='%s'" % '家庭维修'

string = "a.province like '%北京%' "

string = "s.类目 LIKE '%房屋维修%'"
sql = match_workers_from_service_area(area, service)
sql = service_from_workers_name("陈海云")
get_data(sql)


def list_to_json(list):
    result = []
    for i in list:
        data = {}
        data['id']=i[0]
        data['name'] = i[1]
        data['phone'] = i[2]
        data['detail'] = i[3]
        result.append(data)
