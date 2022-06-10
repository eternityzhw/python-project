# -*- coding:utf-8 -*-
import urllib.request
import xlwt
import re
import urllib.parse
import time

header = {
    'Host': 'search.51job.com',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'
}


def getfront(page, item):  # page是页数，item是输入的字符串
    result = urllib.parse.quote(item)  # 先把字符串转成十六进制编码
    ur1 = result + ',2,' + str(page) + '.html'
    ur2 = 'https://search.51job.com/list/000000,000000,0000,00,9,99,'
    res = ur2 + ur1  # 拼接网址
    a = urllib.request.urlopen(res)
    html = a.read().decode('gbk')  # 读取源代码并转为unicode
    html = html.replace('\\', '')  # 将用于转义的"\"替换为空
    html = html.replace('[', '')
    html = html.replace(']', '')
    print(html)
    return html


def getInformation(html):
    reg = re.compile(
        r'"type":"engine_jds".*?"job_href":"(.*?)","job_name":"(.*?)".*?"company_href":"(.*?)","company_name":"(.*?)","providesalary_text":"(.*?)".*?"updatedate":"(.*?)".*?,'
        r'"companytype_text":"(.*?)".*?"jobwelf":"(.*?)".*?"attribute_text":"(.*?)","(.*?)","(.*?)","(.*?)","companysize_text":"(.*?)","companyind_text":"(.*?)"',
        re.S)  # 匹配换行符
    items = re.findall(reg, html)
    print(items)
    return items


def main():
    # 新建表格空间
    excel1 = xlwt.Workbook()
    # 设置单元格格式
    sheet1 = excel1.add_sheet('Job', cell_overwrite_ok=True)
    sheet1.write(0, 0, '序号')
    sheet1.write(0, 1, '职位')
    sheet1.write(0, 2, '公司名称')
    sheet1.write(0, 3, '公司地点')
    sheet1.write(0, 4, '公司性质')
    sheet1.write(0, 5, '薪资')
    sheet1.write(0, 6, '学历要求')
    sheet1.write(0, 7, '工作经验')
    sheet1.write(0, 8, '公司规模')
    sheet1.write(0, 9, '公司福利')
    number = 1
    item = input("请输入需要搜索的职位：")  # 输入想搜索的职位关键字

    for j in range(6, 8):  # 页数
        try:
            print("正在爬取第" + str(j) + "页数据...")
            html = getfront(j, item)  # 调用获取网页原码
            for i in getInformation(html):
                try:
                    sheet1.write(number, 0, number)
                    sheet1.write(number, 1, i[1])
                    sheet1.write(number, 2, i[3])
                    sheet1.write(number, 3, i[8])
                    sheet1.write(number, 4, i[6])
                    sheet1.write(number, 5, i[4])
                    sheet1.write(number, 6, i[10])
                    sheet1.write(number, 7, i[9])
                    sheet1.write(number, 8, i[12])
                    sheet1.write(number, 9, i[7])
                    number += 1
                    excel1.save("1.xls")
                    time.sleep(0.1)
                except:
                    pass
        except:
            pass


if __name__ == '__main__':
    main()
