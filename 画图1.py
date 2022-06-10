# -*- coding: utf-8 -*-
import pandas as pd
import re
from pyecharts import Pie, Funnel, Geo, WordCloud, Page, Bar
import matplotlib.pyplot as plt
import json
from matplotlib import font_manager  # 显示中文

my_font = font_manager.FontProperties(fname="C:\Windows\Fonts\msyh.ttc")
file = pd.read_excel(r'1.xls', sheet_name='Job')
f = pd.DataFrame(file)
pd.set_option('display.max_rows', None)  # 显示所有行
add = f['公司地点']
com = f['公司性质']
sly = f['薪资']
edu = f['学历要求']
exp = f['工作经验']
num = f['公司规模']
wel = f['公司福利']
address = []
company = []
salary = []
min_s = []
max_s = []
education = []
experience = []
number = []
welfare = []
for i in range(0, len(f)):
    try:
        a = add[i].split('-')
        address.append(a[0])
        # print(address[i])
        company.append(com[i])
        # print(company[i])
        s = re.findall(r'\d*\.?\d+', sly[i])
        s1 = float(s[0])
        s2 = float(s[1])
        salary.append([s1, s2])
        min_s.append(s1)
        max_s.append(s2)
        # print(salary[i])
        education.append(edu[i])
        # print(education[i])
        t = re.search(r'\d*', exp[i])
        experience.append(t[0])
        # print(experience[i])
        number.append(num[i])
        # print(number[i])
        c = wel[i].split()
        welfare.extend(c)
        # print(welfare[i])

    except:
        pass

# 折线图
my_df = pd.DataFrame({'experience': experience, 'min_salay': min_s, 'max_salay': max_s})  # 关联工作经验与薪资
data1 = my_df.groupby('experience').mean()['min_salay'].plot(kind='line')
plt.xlabel('experience')
plt.ylabel('min_salay')
plt.savefig('save1.jpg')
plt.show()
data2 = my_df.groupby('experience').mean()['max_salay'].plot(kind='line')
plt.xlabel('experience')
plt.ylabel('max_salay')
plt.savefig('save2.jpg')
plt.show()
my_df2 = pd.DataFrame({'education': education, 'min_salay': min_s, 'max_salay': max_s})  # 关联学历与薪资
data3 = my_df2.groupby('education').mean()['min_salay'].plot(kind='line')
plt.xticks(fontproperties=my_font)
plt.xlabel('education')
plt.ylabel('min_salay')
plt.savefig('save3.jpg')
plt.show()
data4 = my_df2.groupby('education').mean()['max_salay'].plot(kind='line')
plt.xlabel('education')
plt.ylabel('max_salay')
plt.xticks(fontproperties=my_font)
plt.savefig('save4.jpg')
plt.show()


def get_max(list):
    max = {}
    for i in set(list):
        max[i] = list.count(i)
    return max


def get_min(list):
    min = {}
    for i in set(list):
        min[i] = list.count(i)
    return min


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


# 饼状图
dir1 = get_edu(education)
dir2 = get_com(company)
dir3 = get_number(number)
attr = dir1.keys()
value = dir1.values()
pie = Pie("学历要求")
pie.add("", attr, value, center=[50, 50], is_random=False, radius=[30, 75], rosetype='radius',
        is_legend_show=False, is_label_show=True, legend_orient='vertical')
pie.render('学历要求.html')
attr = dir2.keys()
value = dir2.values()
pie = Pie("公司性质")
pie.add("", attr, value, center=[50, 50], is_random=False, radius=[30, 75], rosetype='radius',
        is_legend_show=False, is_label_show=True, legend_orient='vertical')
pie.render('公司性质.html')
attr = dir3.keys()
value = dir3.values()
pie = Pie("公司人数")
pie.add("", attr, value, center=[50, 50], is_random=False, radius=[30, 75], rosetype='radius',
        is_legend_show=False, is_label_show=True, legend_orient='vertical')
pie.render('公司人数.html')
# 漏斗图
dir4 = get_experience(experience)
dir5 = get_edu(education)
attr3 = dir4.keys()
value3 = dir4.values()
funnel = Funnel("工作经验漏斗图", title_pos='center')
funnel.add("", attr3, value3, is_label_show=True, label_pos="inside", label_text_color="#fff", legend_orient='vertical',
           legend_pos='left')
funnel.render('工作经验要求漏斗图.html')
attr3 = dir5.keys()
value3 = dir5.values()
funnel = Funnel("学历要求漏斗图", title_pos='center')
funnel.add("", attr3, value3, is_label_show=True, label_pos="inside", label_text_color="#fff", legend_orient='vertical',
           legend_pos='left')
funnel.render('学历要求漏斗图.html')
dir6 = get_address(address)
attr2 = dir6.keys()
value2 = dir6.values()
geo = Geo("人才需求分布图", title_color="#2E2E2E",
          title_text_size=24, title_top=20, title_pos="center", width=1300, height=600)

geo.add("", attr2, value2, type="effectScatter", is_random=True, visual_range=[0, 1000], maptype='china', symbol_size=8,
        effect_scale=5, is_visualmap=True)
geo.render('人才需求分布图.html')
dir7 = get_welfare(welfare)
attr3 = dir7.keys()
value3 = dir7.values()
# print(attr3)
# print(value3)
page = Page("公司福利")
wordcloud = WordCloud(width=1300, height=620)
wordcloud.add("", attr3, value3, shape='diamond', word_size_range=[12, 60])
page.add(wordcloud)
page.render("公司福利.html")
