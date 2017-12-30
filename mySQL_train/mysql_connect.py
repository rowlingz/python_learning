import pymysql


def inser_mysql(position):
    conn = pymysql.connect(host="192.168.1.105", user="root", password="root", db="crawer", charset="utf8")
    cur = conn.cursor()
    try:
        sql_insert = "insert into position_info (city, position_name, salary, type, detail_info)" \
                     " VALUES (%s, %s, %s, %s, %s)"
        cur.execute(sql_insert, (position['city'], position['position_name'],
                                 position['salary'], position['type'], position['detail_info']))
        conn.commit()
        return True
    except ValueError:
        return False


position_inf = {
    'city': 'nanjing',
    'position_name': '机器学习',
    'salary': 15,
    'type': '数据分析',
    'detail_info': '学习学习'
}


print(inser_mysql(position_inf))