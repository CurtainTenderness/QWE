import requests
import pymysql
from lxml import etree

def tiebaSpider(tiebaName,startPage,endPage):
    url='https://tieba.baidu.com/f?'
    headers = {'User-Agent': 'Mozilla/5.0 (compatible; WOW64; MSIE 10.0; Windows NT 6.2)'}
    for page in range(startPage,endPage+1):
        # 1网页爬取
        pn=(page-1)*50
if __name__=='__main__':
    tiebaName = input('请求输入贴吧名称：')
    startPage = int(input('请输入起始的页码：'))
    endPage = int(input('请输入结束页码：'))
    tiebaSpider(tiebaName, startPage, endPage)