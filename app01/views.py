
from django.shortcuts import render,redirect,HttpResponse
import pymysql
def classes(request):
    # 创建连接
    conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='123', db='s4db65',charset='utf8')
    cursor  =   conn.cursor(cursor=pymysql.cursors.DictCursor)
    # 创建游标
    # cursor = conn.cursor()
    # 执行SQL，并返回收影响行数
    cursor.execute("select id,title from class")
    class_list=cursor.fetchall()
    # 执行SQL，并返回受影响行数
    # effect_row = cursor.execute("update hosts set host = '1.1.1.2' where nid > %s", (1,)
    # 执行SQL，并返回受影响行数
    # effect_row = cursor.executemany("insert into hosts(host,color_id)values(%s,%s)", [("1.1.1.11",1),("1.1.1.11",2)])
    # 提交，不然无法保存新建或者修改的数据
    # conn.commit()
    # 关闭游标
    cursor.close()
    # 关闭连接
    conn.close()
    return render(request,'class.html',{'class_list':class_list})
def ndd_class(request):
    if request.method == "GET":
        return render(request,'ndd_class.html')
    else:
        print(request.POST)
        v = request.POST.get('title')
        if len(v) > 0:
            print("*************",v)
            conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='123', db='s4db65', charset='utf8')
            cursor  =   conn.cursor(cursor=pymysql.cursors.DictCursor)
            # sql = 'insert into class(title) values (%s);'
            # cursor.execute(sql,[v])
            cursor.execute("insert into class(title) values(%s)", [v,])
            conn.commit()
            cursor.close()
            conn.close()
            # cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
            # cursor.execute("insert into class(title) values (%s)",[v,])
            # conn.commit()
            # cursor.close()
            # conn.close()
            return redirect('/classes/')
        else:
            return render(request,'ndd_class.html',{'msg':'班级名称不能为空'})

def del_class(request):
    nid=request.GET.get('nid')
    print(nid)
    conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='123', db='s4db65', charset='utf8')
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
    cursor.execute("delete from class where id = %s", [nid,])
    conn.commit()
    cursor.close()
    conn.close()
    return redirect('/classes/')
def edit_class(request):
    if request.method == "GET":
        nid = request.GET.get('nid')
        conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='123', db='s4db65', charset='utf8')
        cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
        cursor.execute("select id,title from class where id =%s", [nid, ])
        result = cursor.fetchone()
        # conn.commit()
        cursor.close()
        conn.close()
        print(result)
        return render(request,'edit_class.html',{"result":result})
    else:
        nid = request.GET.get('nid')
        title = request.POST.get('title')
        print(nid,title)
        conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='123', db='s4db65', charset='utf8')
        cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
        cursor.execute("update class set title = %s  where id = %s", [title,nid,])
        conn.commit()
        cursor.close()
        conn.close()
        return redirect('/classes/')
def students(request):
    '''
    学生列表
    :param request:封装了请求的所有信息
    :return:
    select student.id,student.name,class.title from student left join class on student.class_id = class.id;
    '''
    conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='123', db='s4db65', charset='utf8')
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
    cursor.execute("select student.id,student.name,class.title from student left join class on student.class_id = class.id")
    student_list = cursor.fetchall()
    cursor.close()
    conn.close()
    return render(request,'students.html',{'student_list':student_list})
# 添加学生列表页
def add_student(request):
    if request.method == "GET":
        conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='123', db='s4db65', charset='utf8')
        cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
        cursor.execute("select id,title from class")
        class_list = cursor.fetchall()
        cursor.close()
        conn.close()
        return render(request,'add_student.html',{'class_list':class_list})
    else:
        name = request.POST.get('name')
        class_id =request.POST.get('class_id')
        conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='123', db='s4db65', charset='utf8')
        cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
        cursor.execute("insert into student(name,class_id)values (%s,%s)",[name,class_id,])
        conn.commit()
        cursor.close()
        conn.close()
        return redirect('/students/')
from utils  import sqlhelper
def edit_student(request):
    if request.method == "GET":
        nid=request.GET.get('nid')
        class_list = sqlhelper.get_lsit("select id,title from class",[])
        curr_student_info=  sqlhelper.get_one('select id,name,class_id from student where id=%s',[nid,])
        return render(request,'edit_student.html',{'class_list':class_list,'curr_student_info':curr_student_info})
    else:
        nid = request.GET.get('nid')
        name = request.POST.get('name')
        class_id = request.POST.get('class_id')
        sqlhelper.modify("update student set name =%s ,class_id=%s where id =%s",[name,class_id,nid,])
        return redirect('/students/')

#     ======对话框添加=================
def modal_add_class(request):
    title = request.POST.get('title')
    if len(title) > 0:
        sqlhelper.modify('insert into class(title) values (%s)',[title,])
        # return redirect('/classes/')
        return HttpResponse('ok')
#     刷新的原因是form表单的提交特性。
    else:
        return HttpResponse('班级标题不能为空')