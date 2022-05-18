import mysql.connector as sql
conn=sql.connect(host="localhost",user="root",passwd="Harshv@8201",database="old")
if conn.is_connected():
    print('successfully connected')
c1=conn.cursor()    
c1.execute('create table cloth(customer_name varchar(50),gender varchar(10),phone_no long,items varchar(20),qty int,payment int)')

