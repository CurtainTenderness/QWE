import requests
from lxml import etree
import pymysql
def down(url):
    '''
    爬取指定url的页面
    :param url:
    :return:
    '''
    headers={'User-Agent':'Mozilla/5.0 (compatible; WOW64; MSIE 10.0; Windows NT 6.2)'}
    response = requests.get(url, headers=headers)
    html = response.content
    return html

def parase(html):
    '''
    进行数据提取
    :return:
    '''
    # 利用etree.HTML，将字符串解析位HTML文档
    html=etree.HTML(html)
    # 将HTML中所有的房子信息都储存在ls中
    ls = html.xpath('//li[@class="clear LOGCLICKDATA"]')
    print(len(ls))
    for item in ls:
        link = item.xpath('.//div[@class="info clear"]/div[@class="title"]/a/@href')[0]
        detail_html=down(link)
        detail_html=etree.HTML(detail_html)
        title=detail_html.xpath('//h1[@class="main"]/text()')[0]
        print('title',title)
        print('link',link)
        unitPrice=detail_html.xpath('//span[@class="unitPriceValue"]')[0].text
        print('单价',unitPrice)
        unit=detail_html.xpath('//span[@class="unitPriceValue"]/i/text()')[0]
        print('单位',unit)
        totalprice=detail_html.xpath('//div[@class= "price "]/span[@class="total"]/text()')[0]
        print('总价',totalprice)
        totalUnit = detail_html.xpath('//div[@class= "price "]/span[@class="unit"]/span/text()')[0]
        print('总价单位：', totalUnit)
        name=detail_html.xpath('//a[@class="info "]/text()')[0]
        print("小区名称",name)
        region=detail_html.xpath('//div[@class="areaName"]/span[@calss="info"]//text()')
        region="".join(region)
        print("所在区域",region)
        bases = detail_html.xpath('//div[@class="base"]/div[@class="content"]/ul/li')
        print('bases len:', len(bases))
        roomtype=bases[0].xpath('./text()')[0]
        print('房间户型',roomtype)
        floor = bases[1].xpath('./text()')[0]
        print('所在楼层', floor)
        roomtype = bases[2].xpath('./text()')[0]
        print('建筑面积', roomtype)
        roomstruct = bases[3].xpath('./text()')[0]
        print('户型结构', roomstruct)
        withinarea = bases[4].xpath('./text()')[0]
        print('套内面积', withinarea)
        buildingtype = bases[5].xpath('./text()')[0]
        print('建筑类型', buildingtype)
        roomdir = bases[6].xpath('./text()')[0]
        print('房屋朝向', roomdir)
        buildstruc = bases[7].xpath('./text()')[0]
        print('建筑结构', buildstruc)
        decorate = bases[8].xpath('./text()')[0]
        print('装修情况', decorate)
        elevator = bases[9].xpath('./text()')[0]
        print('户梯比例', elevator)
        haselevator = bases[10].xpath('./text()')[0]
        print('配备电梯', haselevator)
        interest = bases[11].xpath('./text()')[0]
        print('产权年限', interest)
        params = [title, link, unitPrice, unit, totalprice, totalUnit, name, region, roomtype, floor, withinarea, roomstruct,
                  withinarea, buildingtype, roomdir, buildstruc, decorate, elevator, haselevator, interest]
        # 将数据添加到数据库中
        saveData(params)
        print('='*60)

# 存储数据
def saveData(data):
    '''
    数据存储
    :param data:
    :return:
    '''
    # 与表连接
    strSql='insert into lianjia VALUES(0,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
    cur.execute(strSql,data)
    # 提交
    conn.commit()

if __name__=="__main__":
    # 连接数据库
    conn=pymysql.connect(host='127.0.0.1',port=3306,user='root',password='123456',db='dblianjia')
    cur = conn.cursor()
    for page in range(1,5):
        if page==1:
            url='https://sh.lianjia.com/ershoufang/'
        else:
            url='https://sh.lianjia.com/ershoufang/pg'+str(page)+'/'
        html = down(url)
        parase(html)
