import pandas as pd
from flask import request, render_template, session, redirect
from flask_sqlalchemy import SQLAlchemy

import sql
from dangdang_1 import dd_sc
from jingdong_1 import jd_sc
from static.blue_properties import properties_blue
from taobao_1 import tb_sc
from sqlalchemy import create_engine


@properties_blue.route('/properties', methods=['GET', 'POST'])  # details
def properties():
    if request.method == 'POST':
        value = request.form.to_dict()
        conn = create_engine('mysql+pymysql://root:1234@127.0.0.1:3306/diploma?charset=utf8')
        values = value['keys']
        print(sql.mysql_user_select_alldata(session.get("name"))[0][2])
        # a = float(sql.mysql_user_select_alldata(session.get("name"))[0][2])
        # b = float(sql.mysql_user_select_alldata(session.get("name"))[0][3])
        # c = float(sql.mysql_user_select_alldata(session.get("name"))[0][4])
        # print(values)
        # tb_data = tb_sc(values,a,b,c)
        # jd_data = jd_sc(values,a,b,c)
        # dd_data = dd_sc(values,a,b,c)
        # sum_df = pd.concat([dd_data,jd_data,tb_data],axis=0)
        # sum_fdf = sum_df.sort_values(by='score')
        # try:
        #     #     sum_df.to_sql("test", con=conn, schema=None, if_exists='append', index=False)
        #     sum_fdf.to_sql("test", con=conn, schema=None, if_exists='replace', index=False)
        # except Exception as e:
        #     print(e)
        # data = sql.mysql_select_other()
        data = sql.mysql_select_other_test()
        sum_data = []
        print(len(data))
        for i in range(len(data)):
            sum_data.append({})
            sum_data[i]['name'] = data[i][0]
            sum_data[i]['price'] = data[i][1]
            sum_data[i]['brand'] = data[i][2]
            sum_data[i]['discuss'] = data[i][3]
            sum_data[i]['url'] = data[i][4]
            sum_data[i]['type'] = data[i][5]
        return render_template("./html/properties_2.html", sum_data=sum_data)
    else:
        return redirect("/")
