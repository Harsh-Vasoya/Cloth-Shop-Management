import mysql.connector as sql
conn=sql.connect(host="localhost",user="root",passwd="Harshv@8201",database="old")
if conn.is_connected():
    print('successfully connected')
c1=conn.cursor()    
c1.execute('create table comment(comment varchar(200))')


