import requests
import pymysql
from lxml import etree

def down(url):
    headers={'User-Agent':'Mozilla/5.0 (compatible; WOW64; MSIE 10.0; Windows NT 6.2)'}
    reponse=requests.get(url,headers=headers)
    # 连接
    html=reponse.content
    return html

def parase(html):
    html=etree.HTML(html)
    # contains查找id中包含qiushi_tag_的内容
    ls=html.xpath('//div[@class="recommend-article"]/ul/li[contains(@id,"qiushi_tag_")]')
    print(len(ls))
    # print(ls)

    for i in ls:
        link=i.xpath('.//a[@class="recmd-user"]/img/@src')
        print('用户头像链接：',link)
        name=i.xpath('.//span[@class="recmd-name"]/text()')
        print("用户名：",name)
        content = i.xpath('.//a[@class="recmd-content"]/text()')
        print('内容：', content)
        haoxiao=i.xpath('.//div[@class="recmd-num"]/span/text()')[0]
        print("好笑，点赞：",haoxiao)
        review=i.xpath('.//div[@class="recmd-num"]/span/text()')[3]
        print('评论：',review)
        params=[link,name,content,haoxiao,review]
        saveData(params)
        print('*'*60)

def saveData(data):
    str='insert into baike VALUES(0,%s,%s,%s,%s,%s)'
    cur.execute(str,data)
    conn.commit()


if __name__=="__main__":
    # 链接数据库
    conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='123456', db='dblianjia')
    cur=conn.cursor()
    for page in range(1,2):
        url = 'https://www.qiushibaike.com/8hr/page/' + str(page) + '/'
        print(url)
        html = down(url)
        parase(html)