# -*- utf-8 -*-
import pymysql

conn = pymysql.connect(host="localhost", user="root", password="root", database="test", port=3306, charset="utf8")
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

sql10 = "SELECT s_score FROM score ORDER BY s_score DESC "

sql11 = "SELECT * FROM movie LIMIT 10"

sql12 = "SELECT realIP FROM all_gzdata WHERE userOS IN ('Android', 'Windows 7') LIMIT 10 "

sql13 = "SELECT * FROM teacher WHERE t_id NOT BETWEEN 1 and 3"

sql14 = "SELECT t_id as number, t_name as name FROM teacher"

sql15 = "SELECT student.s_name, score.c_id, score.s_score FROM student LEFT JOIN score ON student.s_id =score.s_id"

sql16 = "SELECT student.s_name, score.s_score FROM student LEFT JOIN score ON student.s_id = score.s_id"

sql17 = "SELECT t_id, t_name FROM teacher UNION SELECT t_id, t_name FROM teacher1"

sql18 = "SELECT s_id, AVG(s_score) FROM score GROUP BY s_id"

sql19 = "SELECT s_id, SUM(s_score) FROM score GROUP BY s_id HAVING SUM(s_score) > 100 "

sql20 = "SELECT t_id, UCASE(t_name) AS name FROM teacher1"

sql21 = "SELECT MID(t_name, 1, 2) FROM teacher1"

cur.execute(sql20)
conn.commit()

print(cur.fetchall())
cur.close()

