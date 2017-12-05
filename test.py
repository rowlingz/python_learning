import pymysql

# 创建连接，连接mySOL中的某一数据库（db)
conn = pymysql.connect(host='localhost', user='root', password='root', db='njust', port=3306)

# 创建游标，获取连接的cursor，执行后续操作
cur = conn.cursor()


# 查询操作
sql = "select * from teacher"       # sql语句
cur.execute(sql)                    # cur执行sql语句


# 获取结果的第一行数据
row_1 = cur.fetchone()
print(row_1)

# 获取结果的前n行数据
# row_2 = cur.fetchmany(2)

# 获取结果的所有行数据，储存在元祖中
# rows = cur.fetchall()
# for row in rows:
#     print(row)


# # 获取结果集的条数-字符串类型
# numrows = cur.rowcount
# print(numrows)
#
# # 获取结果集的描述信息
# des = cur.description
# print(des)


# 插入数据
sql_insert = "insert into teacher values ( '5','lucy', '6')"
cur.execute(sql_insert)

conn.commit()       # 提交数据，用于更新数据库

# 修改数据
sql_change = "update teacher set NAME='kite' WHERE id=6"
cur.execute(sql_change)
conn.commit()

# 删除数据
sql_delet = "delete from teacher WHERE id=7 "
cur.execute(sql_delet)
conn.commit()

cur.close()     # 关闭游标对象
conn.close()    # 关闭连接




