import mysql.connector

mydb = mysql.connector.connect(host='localhost', user= 'nelson', passwd = '9894883980', database = 'nelson')

mycursor = mydb.cursor()
mycursor.execute("update student set college = 'madras university' where name = 'Nelson'")

mycursor.execute("update student set college = 'anna univ' where name = 'Nelson'")
mycursor.execute("select * from student")
result = mycursor.fetchall()

for i in result:
    print(i)
