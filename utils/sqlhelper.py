import pymysql

def get_lsit(sql,args):
    #学生列表页
    conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='123', db='s4db65', charset='utf8')
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
    cursor.execute(sql,args)
    result = cursor.fetchall()
    cursor.close()
    conn.close()
    return result
def get_one(sql,args):
    #提取一条信息
    conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='123', db='s4db65', charset='utf8')
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
    cursor.execute(sql, args)
    result = cursor.fetchone()
    cursor.close()
    conn.close()
    return result

def  modify(sql,args):
    #提交
    conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='123', db='s4db65', charset='utf8')
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
    cursor.execute(sql,args)
    conn.commit()
    cursor.close()
    conn.close()
