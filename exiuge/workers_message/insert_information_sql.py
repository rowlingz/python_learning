# -*- coding:utf-8 -*-

# 插入信息
import pymysql


class Insert_Message:
    def __init__(self):
        conn = pymysql.connect(host="127.0.0.1",
                               user="root",
                               password="root",
                               database="premetheus",
                               port=3306,
                               charset='utf8')
        self.conn = conn

    def insert_workers(self, string):
        """插入 师傅表"""
        conn = self.conn
        cur = conn.cursor()
        keys = [str(k) for k in string.keys()]
        values = tuple(string.values())
        keys = ', '.join(keys)

        sql_check = "SELECT * FROM workers WHERE 身份证号 = %s "
        sql_insert = "INSERT INTO workers (%s) VALUES %s " % (keys, values)

        try:
            cur.execute(sql_check, string['身份证号'])
            if cur.rowcount != 0:
                print("该信息已存在")
            else:
                cur.execute(sql_insert)
                conn.commit()
                print("插入成功")
        except Exception as e:
            print("插入失败： " + str(e))
        finally:
            cur.close()
            conn.close()

    def insert_workers_area(self, string):
        """插入 师傅-地区表"""
        conn = self.conn
        cur = conn.cursor()
        id = string['身份证号']
        areas = string['area']

        sql_check_worker_area = "SELECT * FROM area, workers, workers_area wa " \
                                "WHERE wa.area_id=area.id AND wa.workers_id=workers.id " \
                                "AND area.province = %s AND area.city= %s AND area.county = %s AND workers.身份证号 = %s "

        sql_insert_worker_area = "INSERT INTO workers_area (area_id, workers_id) " \
                                 "(SELECT area.id, workers.id FROM area, workers " \
                                 "WHERE area.province = %s AND area.city= %s AND area.county = %s " \
                                 "AND workers.身份证号 = %s )"

        try:
            for area in areas:
                area['id'] = id
                infor = tuple(area.values())

                cur.execute(sql_check_worker_area, infor)
                if cur.rowcount != 0:
                    print(area['区'] + ' 已经存在')
                    break
                else:
                    cur.execute(sql_insert_worker_area, infor)

                if cur.rowcount == 0:
                    # print(area)
                    raise Exception(area)
                else:
                    conn.commit()
            print('插入结束')
        except Exception as e:
            print("插入失败： " + str(e))
        finally:
            cur.close()
            conn.close()

    def insert_workers_service(self, string):
        """插入 师傅-服务表"""
        conn = self.conn
        cur = conn.cursor()
        id = string['身份证号']
        services = string['service']

        sql_check_worker_sevice = "SELECT * FROM service, workers, workers_service ws " \
                                  "WHERE service.id=ws.service_id AND workers.id=ws.workers_id " \
                                  "AND service.详情 = %s AND workers.身份证号 = %s "

        sql_insert_worker_service = "INSERT INTO workers_service (service_id, workers_id) " \
                                    "(SELECT service.id, workers.id FROM service, workers " \
                                    "WHERE service.详情 = %s AND workers.身份证号 = %s)"

        try:
            for service in services:
                cur.execute(sql_check_worker_sevice, ((service['详情'], id)))

                if cur.rowcount != 0:
                    print(service['详情'] + ' 已经存在')
                    break
                else:
                    cur.execute(sql_insert_worker_service, (service['详情'], id))

                if cur.rowcount == 0:
                    # print(service)
                    raise Exception([service, id])
                else:
                    conn.commit()
            print('插入结束')
        except Exception as e:
                print("插入失败： " + str(e))
        finally:
            cur.close()
            conn.close()


string = {'姓名': '张永旺', '电话': '18100276558', '身份证号': '51282519720801733x',
          'area': [{'省': '四川省', '市': '成都市', '区': '金牛区'}],
          'service': [{'主类别': '家庭维修', '类目': '房屋维修', '详情': '防水补漏'}]}

service = {'主类别': '家庭维修', '类目': '屋维修', '详情': ' '}


# insert = Insert_Message()
# # insert_workers_area(string)
# insert.insert_workers_service(string)


#
# sql = "SELECT * FROM area WHERE province LIKE %s"
# conn = pymysql.connect(host="127.0.0.1",
#                        user="root",
#                        password="root",
#                        database="premetheus",
#                        port=3306,
#                        charset='utf8')
#
# cur = conn.cursor()
#
# cur.execute(sql, '%' + '北京' + '%')
# print(cur.fetchall())

