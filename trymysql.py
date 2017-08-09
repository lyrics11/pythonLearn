import pymysql.cursors

#连接数据库
connect=pymysql.connect(
    host='localhost',
    port=3306,
    user='root',
    passwd='root',
    db='ly',
    charset='utf8'
)

cursor=connect.cursor()
#查询
sql="SELECT * FROM student"
cursor.execute(sql)
numrows=int(cursor.rowcount)
for i in range(numrows):
    row=cursor.fetchone()
    print (row[0],row[1],row[2],row[3],row[4])
#插入
sql="INSERT INTO student(name,age,score) VALUES ('%s','%d','%d')"
data=('Eric',66,88)
cursor.execute(sql % data)
connect.commit()
#update
sql="UPDATE student SET age=%d where name='%s'"
data=(16,'liuyang')
cursor.execute(sql % data)
connect.commit()
#删除
sql="DELETE FROM student WHERE name='%s'"
data='Eric'
cursor.execute(sql % data)
connect.commit()
#插入
sql="INSERT INTO student(name,age,score,class) VALUES ('%s','%d','%d','%d')"
data=('Eric',66,88,1)
cursor.execute(sql % data)
connect.commit()
#内连接
sql="SELECT student.`name`,teacher.`name` FROM student INNER JOIN teacher ON student.`class`=teacher.`class` AND student.`class`=1"
cursor.execute(sql)
row=cursor.fetchall()
print(row)
connect.commit()

cursor.close()
connect.close()