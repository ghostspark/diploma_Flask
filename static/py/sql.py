import pymysql as sql


# 增
def mysql_insert(data):  # 用户插入/注册
    db = sql.connect(
        host="127.0.0.1",
        port=3306,
        user="root",
        password="1234",
        database='diploma'
    )
    test_data = data
    cursor = db.cursor()
    value = [(test_data[0]['name'], test_data[0]['pw'], test_data[0]['e_mail'])]
    try:
        cursor.executemany("insert into user_test(user_name, user_pw, user_email) values(%s,%s,%s);", value)
        db.commit()
        print('success')
    except:
        db.rollback()
        print('fail')

    db.close()


# 查
def mysql_select_user(name):  # 查找用户
    db = sql.connect(
        host="127.0.0.1",
        port=3306,
        user="root",
        password="1234",
        database='diploma'
    )
    cursor = db.cursor()
    s = "select * from user_test where user_name='{}';".format(name)
    try:
        cursor.execute(s)
        data = cursor.fetchall()
        id = data[0][1]
        pw = data[0][2]
        email = data[0][3]
        power = data[0][4]
        return id, pw, email, power
    except:
        id = pw = power = email = 3
        return id, pw, email, power
    db.close()


def mysql_root_select_alluser():  # 查找用户
    db = sql.connect(
        host="127.0.0.1",
        port=3306,
        user="root",
        password="1234",
        database='diploma'
    )
    cursor = db.cursor()
    s = "SELECT user_test.user_name, user_test.user_pw, user_test.user_email FROM user_test;"
    try:
        cursor.execute(s)
        data = cursor.fetchall()
        return data
    except:
        data = 'null'
        return data
    db.close()


def mysql_user_select_alldata(name):  # 查找用户
    db = sql.connect(
        host="127.0.0.1",
        port=3306,
        user="root",
        password="1234",
        database='diploma'
    )
    cursor = db.cursor()
    s = "SELECT user_test.user_name, user_test.user_email, a, b, c FROM " \
        "user_test where user_name = '{}';".format(name)
    try:
        cursor.execute(s)
        data = cursor.fetchall()
        return data
    except:
        data = 'null'
        return data
    db.close()


def mysql_select_other():  # 查找商品
    db = sql.connect(
        host="127.0.0.1",
        port=3306,
        user="root",
        password="1234",
        database='diploma'
    )
    cursor = db.cursor()
    s = "select name,price,brand,discuss,url,type from sum_data ;"
    try:
        cursor.execute(s)
        data = cursor.fetchall()
        return data
    except:
        data = ('/')
        return data
    db.close()


def mysql_select_other_test():  # 查找商品-测试用
    db = sql.connect(
        host="127.0.0.1",
        port=3306,
        user="root",
        password="1234",
        database='diploma'
    )
    cursor = db.cursor()
    s = "select name,price,brand,discuss,url,type from test2 ;"
    try:
        cursor.execute(s)
        data = cursor.fetchall()
        return data
    except:
        data = ('/')
        return data
    db.close()



# 删
def mysql_user_delete(u_name):  # 删除用户
    db = sql.connect(
        host="127.0.0.1",
        port=3306,
        user="root",
        password="1234",
        database='diploma'
    )
    cursor = db.cursor()
    s = "delete from user_test where user_name = '{}'".format(u_name)
    try:
        cursor.execute(s)
        db.commit()
        print('success')
    except Exception as e:
        db.rollback()
        print('fail')
        print(e)

    db.close()


# 改
def mysql_userpw_alter(u_name, new_pw):  # 更改用户-密码
    db = sql.connect(
        host="127.0.0.1",
        port=3306,
        user="root",
        password="1234",
        database='diploma'
    )
    cursor = db.cursor()
    s = "update user_test set user_pw ='{}' where user_name = '{}';".format(new_pw, u_name)
    print(s)
    try:
        cursor.execute(s)
        db.commit()
        print('success')
    except Exception as e:
        db.rollback()
        print('fail')
        print(e)
    db.close()


def mysql_email_alter(u_name, new_email):  # 更改-邮箱
    db = sql.connect(
        host="127.0.0.1",
        port=3306,
        user="root",
        password="1234",
        database='diploma'
    )
    cursor = db.cursor()
    s = "update user_test set user_email ='{}' where user_name = '{}'".format(new_email, u_name)
    try:
        cursor.execute(s)
        db.commit()
        print('success')
    except:
        db.rollback()
        print('fail')
    db.close()
