import pymysql


conn = pymysql.connect(host='localhost', user='root', password='root', db='njust', port=3306)
cursor = conn.cursor()
cursor.execute("select * from teacher")


row_1 = cursor.fetchone()
print(row_1)


