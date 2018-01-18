import pymysql

conn = pymysql.connect(host="localhost", user="root", password="root", database="test", port=3306)
cur = conn.cursor()

sql = "select a.s_id from (select s_id, s_score from score where c_id = '1' )a, " \
      "(select s_id, s_score from score where c_id = '2')b " \
      "where a.s_score > b.s_score and a.s_id = b.s_id"


sql2 = "SELECT s_id, AVG(s_score) FROM score GROUP BY s_id HAVING AVG (s_score) > 60"

sql3 = "SELECT student.s_id, student.s_name, count(score.c_id), sum(s_score) FROM student LEFT JOIN score ON " \
       "student.s_id = score.s_id GROUP BY student.s_id, s_name"

sql4 = "SELECT count(distinct(t_name)) FROM teacher WHERE t_name LIKE '李%'"

sql5 = "SELECT MAX(s_score), MIN(s_score), c_id AS coure_id FROM score  GROUP BY c_id"

sql6 = "SELECT s_id, c_id FROM score WHERE s_score BETWEEN 70 AND 80"

sql7 = "INSERT INTO score (s_id, s_score) VALUES (3, 60) "

sql8 = "UPDATE score SET c_id = 1 WHERE s_id = 3 AND s_score = 60"

sql9 = "SELECT TOP 2 * FROM score WHERE s_id = 1"

cur.execute(sql9)
conn.commit()

print(cur.fetchall())
cur.close()

