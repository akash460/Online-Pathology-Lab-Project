#!C:\Users\A\AppData\Local\Programs\Python\Python38\python.exe
#print('Content-type:text/html\r\n\r\n')
import cgi
import mysql.connector
t =cgi.FieldStorage()
a =t.getvalue('a')
b =t.getvalue('b')
c =t.getvalue('c')
d =t.getvalue('d')
e =t.getvalue('e')
f =t.getvalue('f')
g =t.getvalue('g')
j =t.getvalue('j')
db=mysql.connector.connect(host="localhost",user="root",passwd="",db="project")
cur=db.cursor()
cur.execute("insert into aregister(name,email,phone,specialnote,way,day,time,did)values('%s','%s','%s','%s','%s','%s','%s','%s')"%(a,b,c,d,e,f,g,j))
db.commit()
print("location:index.html?msg=done\r\n\r\n")
