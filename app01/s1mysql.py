import pymysql
# name = input("请输入名字:")
# pwd = input("请输入密码:")
conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='123', db='s4db65', charset='utf8')
cursor = conn.cursor()
sql = 'insert into class(title) values (%s);'
title='全站山崎'
# pwd= "7755"

cursor.execute(sql,[title])
conn.commit()
print("chenggong ")
cursor.close
conn.close()
# if ret:
#     print("登录成功")
# else:
#     print("登录失败")