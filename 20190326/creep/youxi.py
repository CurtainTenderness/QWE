import requests
from lxml import etree
from time import sleep
import csv
import codecs
import random
# 爬取路径
url='http://www.4399.com/?haoqqdh'
# 表头，不同浏览器需要的表头可能不同
headers = {'User-Agent':'Mozilla/5.0 (compatible; WOW64; MSIE 10.0; Windows NT 6.2)'}

response=requests.get(url,headers=headers)
# 提取整个HTML
html=response.content.decode('gbk')
# print(html)
# 将HTML文件存储到一个文件中
s=etree.HTML(html)
# print(type(s))
# 1手游
shouyou=s.xpath('//a[@class="for_phone"]/text()')[0]
shouyou_content=s.xpath("//ul[@class='mi_ul']/li/a/text()")
# print(shouyou,":",shouyou_content)

#2 专辑，儿童，动作，射击，益智，体育等等
ls=s.xpath("//div[@class='mi-lr']")
for i in ls:
    # 【0】代表第一个
    result1=i.xpath(".//a[@class='mi_tit']/text()")[0]
    # 没有加【0】代表爬取所有的
    result1_content=i.xpath(".//div[@class='mi_d']/span/a/text()")
    # print(result1,':',result1_content)

# 3 女生，合辑，H5游戏
ls1=s.xpath("//div[@class='middle_2']/div[5]/a/text()")[0]
ls2=s.xpath("//div[@class='middle_2']/div[6]/a/text()")[0]

ls4=s.xpath("//div[@class='middle_2']/div[8]/a/text()")[1]
# print(ls1,ls2,ls4)
ls0_content=s.xpath("//div[@class='mi_g']")
for i in ls0_content:
    a=i.xpath(".//span/a/text()")
    # print(a)

# 4 网页游戏
ls3=s.xpath("//div[@class='middle_2']/div[7]/a/text()")[1]
# print(ls3)
b=s.xpath("//div[@class='mi_web']/span/a/text()")
# print(b)

# 5 最新好玩小游戏列表
lsa=s.xpath("//div[@class='tm_tit']/a[@class='tit_a']/text()")[0:3]
# print(lsa)
lsa1=s.xpath("//div[@class='box_c']//ul[@class='tm_list']")

# print(type(lsa1))
for i in lsa1:
    c=i.xpath("./li/a/text()")
    # print(c)


# 6 最新推荐游戏
lr=s.xpath(".//a[class='tit_a']/text()")
print(lr)
ls6=s.xpath("//ul[@class='tm_list lf_ul']")[0]
ls6_content=ls6.xpath("./li")
base_url="http://www.4399.com/"
list1=[]
for i in ls6_content:
    ls6_title=i.xpath('./a/text()')[0]
    # print(ls6_title)
    content_url=i.xpath('./a/@href')[0]
    url=base_url+content_url
    # print(url)

    list1.append([ls6_title,url])
print(list1)