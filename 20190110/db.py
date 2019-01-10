# python3 不支持安装 pip install mysqldb
# pip install pymysql
import pymysql # 导入模块驱动

# 创建连接 ip username password dbname
db = pymysql.connect('47.98.217.19','root','1583297240','netshop')
# 使用cursor()方法获取操作游标
cursor = db.cursor()
# 使用execute方法执行SQL语句
cursor.execute("SELECT VERSION()")

# 使用 fetchone() 方法获取一条数据库。
data = cursor.fetchone()

print ("Database version : %s " % data)  # Database version : 5.7.22


cursor.execute('DROP TABLE IF EXISTS EMPLOYEE')

sql = '''CREATE TABLE EMPLOYEE (
         FIRST_NAME  CHAR(20) NOT NULL,
         LAST_NAME  CHAR(20),
         AGE INT,  
         SEX CHAR(1),
         INCOME FLOAT )'''

cursor.execute(sql)
sql = ''' INSERT INTO EMPLOYEE(FIRST_NAME,
         LAST_NAME, AGE, SEX, INCOME)
         VALUES ('Mac', 'Mohan', 20, 'M', 2000)'''
try:
    cursor.execute(sql)
    #提交事务
    db.commit()
except:
    #回滚事务
    db.rollback()

sql = '''select * from EMPLOYEE'''
cursor.execute(sql)
cursor.fetchall()
# 关闭数据库连接
db.close()