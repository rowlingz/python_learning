# coding:utf-8
import timeit
import json
import pymysql
import pandas as pd


# 定义函数批量插入数据
def insert_data_table(message):
    """将数据插入到MySQL中"""
    coon = pymysql.connect(
        host="localhost",
        user="root",
        password="root",
        database="test",
        port=3306,
        charset="utf8")
    sql_insert = "INSERT INTO data (use_id, name, email, age) " \
                 "VALUES (%s, %s, %s, %s)"
    cur = coon.cursor()
    try:
        cur.executemany(sql_insert, message)
        coon.commit()
    except Exception as e:
        print(e)
    finally:
        cur.close()
        coon.close()


# 1、从10个文件中依次录入数据
filename = "data%d.txt"
for i in range(10):
    content = []
    start = timeit.default_timer()
    file = filename % i
    with open(file) as file_object:
        # 从每个文件中读出数据并转换成字典形式，筛选出values
        lines = file_object.readlines()
        for line in lines:
            message = json.loads(line)
            content.append((message['id'], message['name'], message['email'], message['age']))
        # 调用函数完成数据入库
    insert_data_table(content)
    print(file + "完成")
    print(timeit.default_timer() - start)
print("插入完成 " + str(timeit.default_timer()))


conn = pymysql.connect(host="localhost",
                       user="root",
                       password="root",
                       database="test",
                       port=3306,
                       charset="utf8")

total = pd.read_sql("SELECT * FROM data", conn)
total_count = total.shape[0]
print(total_count)

# 2、数据筛选
start = timeit.default_timer()
cur = conn.cursor()
# 删除age < 0
cur.execute("DELETE FROM DATA WHERE age <= 0")
count_age = cur.rowcount
print(count_age)
conn.commit()
cur.close()

# 删除use_id重复项，留下id最小的一项
cur = conn.cursor()
try:
    cur.execute("create table tmp as select min(id) as col1 from data group by use_id HAVING COUNT(use_id > 1)")
    cur.execute("DELETE FROM data WHERE use_id in "
                "(SELECT w.use_id FROM (SELECT a.use_id FROM data a GROUP BY a.use_id HAVING COUNT(a.use_id) > 1) w) "
                "AND id NOT IN (select col1 from tmp)")
    count_use_id = cur.rowcount
    print(count_use_id)
    cur.execute("drop table tmp")
    conn.commit()
except Exception as e:
    print(e)
finally:
    cur.close()

# 删除email格式不正确项
cur = conn.cursor()
cur.execute("DELETE FROM data WHERE email NOT LIKE '%@example.com'")
count_email = cur.rowcount
print(count_email)
cur.close()
conn.commit()
print("筛选结束")
print(timeit.default_timer() - start)


# 统计数据总量
start = timeit.default_timer()
df = pd.read_sql("SELECT * FROM data", conn)
conn.close()

# print(df.head())
# print(df.tail())
print(df.shape)
remain_count = df.shape[0]
delete_count = count_age + count_use_id + count_email

print(remain_count)
print(delete_count)
print("统计结束")
print(timeit.default_timer() - start)