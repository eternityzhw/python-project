# -*- coding: utf-8 -*-
import pandas as pd
import re
from pyecharts.charts import Funnel,Pie,Geo
import matplotlib.pyplot as plt
from pyecharts import options as opts
from pyecharts.datasets import register_url
import matplotlib.pyplot as plt
from pyecharts.components import Table
from pyecharts.options import ComponentTitleOpts
file = pd.read_excel(r'1.xls', sheet_name='Job')
f = pd.DataFrame(file)
pd.set_option('display.max_rows', None)
job = f['职位']
nam = f['公司名称']
add = f['公司地点']
com = f['公司性质']
sly = f['薪资']
edu = f['学历要求']
exp = f['工作经验']
num = f['公司规模']
wel = f['公司福利']
job_name = []
com_name = []
address = []
company = []
salary = []
min_s = []
max_s = []
education = []
experience = []
whole_exp = []
number = []
whole_wel = []
welfare = []
for i in range(0, len(f)):
    try:
        job_name.append(job[i])
        com_name.append(nam[i])
        a = add[i].split('-')
        address.append(a[0])
        # print(address[i])
        company.append(com[i])
        # print(company[i])
        salary.append(sly[i])
        s = re.findall(r'\d*\.?\d+', sly[i])
        s1 = float(s[0])
        s2 = float(s[1])
        #salary.append([s1, s2])
        min_s.append(s1)
        max_s.append(s2)
        # print(salary[i])
        education.append(edu[i])
        # print(education[i])
        whole_exp.append(exp[i])
        t = re.search(r'\d*', exp[i])
        experience.append(t[0])
        # print(experience[i])
        number.append(num[i])
        # print(number[i])
        whole_wel.append(wel[i])
        c = wel[i].split()
        welfare.extend(c)
        # print(welfare[i])

    except:
        pass
"""
#折线图
my_df = pd.DataFrame({'experience':experience, 'min_salay' : min_s, 'max_salay' : max_s})             #关联工作经验与薪资
data1 = my_df.groupby('experience').mean()['min_salay'].plot(kind='line')
plt.xlabel('experience')
plt.ylabel('min_salay')
#plt.savefig('save1.jpg')
plt.show()
data2 = my_df.groupby('experience').mean()['max_salay'].plot(kind='line')
plt.xlabel('experience')
plt.ylabel('max_salay')
#plt.savefig('save2.jpg')
plt.show()
my_df2 = pd.DataFrame({'education':education, 'min_salay' : min_s, 'max_salay' : max_s})              #关联学历与薪资
data3 = my_df2.groupby('education').mean()['min_salay'].plot(kind='line')
plt.xlabel('education')
plt.ylabel('min_salay')
#plt.savefig('save3.jpg')
plt.show()
data4 = my_df2.groupby('education').mean()['max_salay'].plot(kind='line')
plt.xlabel('education')
plt.ylabel('max_salay')
#plt.savefig('save4.jpg')
plt.show()"""


def get_edu(list):
    education2 = {}
    for i in set(list):
        education2[i] = list.count(i)
    return education2


def get_com(list):
    comp = {}
    for i in set(list):
        comp[i] = list.count(i)
    return comp


def get_experience(list):
    experience2 = {}
    for i in set(list):
        experience2[i] = list.count(i)
    return experience2


def get_number(list):
    number = {}
    for i in set(list):
        number[i] = list.count(i)
    return number


def get_address(list):
    address2 = {}
    for i in set(list):
        address2[i] = list.count(i)
    return address2


def get_welfare(list):
    welfare = {}
    for i in set(list):
        welfare[i] = list.count(i)
    return welfare
dir2 = get_address(address)
#print(dir2)
attr2 = dir2.keys()
value2 = dir2.values()
c = (
    Geo()
    .add_schema(maptype="china")
    .add("岗位", [list(z) for z in zip(attr2, value2)])
    .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
    .set_global_opts(
        visualmap_opts=opts.VisualMapOpts(), title_opts=opts.TitleOpts(title="人才需求分布图")
    )
    .render("人才需求分布图.html")
)

table=Table()
headers = ["职位", "公司名称", "公司地点", "公司性质","薪资","学历要求","工作经验","公司规模","公司福利"]
table.add(headers,[list(z) for z in zip(job_name,com_name,address,company,salary,education,whole_exp,number,whole_wel)])
table.set_global_opts(
    title_opts=ComponentTitleOpts(title="招聘数据显示")
)
table.render('招聘数据显示.html')