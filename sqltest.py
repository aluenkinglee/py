#encoding=utf-8
import sys
import MySQLdb

reload(sys)
sys.setdefaultencoding('utf-8')

db=MySQLdb.connect(user='root',charset='utf8',passwd='123',host='localhost',)
cur=db.cursor()
cur.execute('use books')
cur.execute('select * from books_publisher')

f=file("/home/king/workspace/py/tem.txt",'w')

for i in cur.fetchall():
    f.write(i[1])
    f.write(" ")

f.close()
cur.close()
