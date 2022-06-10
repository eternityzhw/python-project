import os
import sys


sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/../')
from flask import Flask, render_template, request, redirect

app = Flask(__name__)  # 寻找工程目录


@app.route('/')#路由匹配根目录
def index():
    return render_template('index.html')


@app.route('/pic1')
def pic1():
    return render_template('公司人数.html', title='公司人数')


@app.route('/pic2')
def pic2():
    return render_template('公司性质.html', title='公司性质')


@app.route('/pic3')
def pic3():
    return render_template('公司福利.html', title='公司福利')


@app.route('/pic4')
def pic4():
    return render_template('学历要求.html', title='学历要求')


@app.route('/pic5')
def pic5():
    return render_template('工作经验要求漏斗图.html', title='工作经验要求漏斗图')


@app.route('/pic6')
def pic6():
    return render_template('学历要求漏斗图.html', title='学历要求漏斗图')


@app.route('/pic7')
def pic7():
    return render_template('1.html', title='薪资与经验折线图')


@app.route('/pic8')
def pic8():
    return render_template('2.html', title='薪资与学历折线图')


@app.route('/pic9')
def pic9():
    return render_template('人才需求分布图.html', title='人才需求分布图')


@app.route('/pic10')
def pic10():
    return render_template('招聘数据显示.html', title='招聘数据显示')


if __name__ == "__main__":
    app.run(host='127.0.0.1', debug=True)
