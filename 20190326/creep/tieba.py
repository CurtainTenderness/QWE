# from lxml import etree
# import requests
# from time import sleep
# import random
# import csv
# import codecs
# def tiebaSpider(teibarName,startPage,endPage):
#     '''
#     批量爬取指定贴吧的页面内容
#     :param teibarName:
#     :param startPage:
#     :param endPage:
#     :return:
#     '''
#     url = 'https://tieba.baidu.com/f?'
#     headers = {'User-Agent':'Mozilla/5.0 (compatible; WOW64; MSIE 10.0; Windows NT 6.2)'}
#     for page in range(startPage,endPage+1):
#         # 1、网页爬取
#         pn = (page-1) * 50
#         params = {
#             'kw':tiebaName,
#             'pn':pn
#         }
#         print('爬取页面：',page)
#         response  = requests.get(url,params=params,headers=headers)
#         html = response.content.decode()
#         print(html)
#         # filename = './data/第'+str(page)+'页.html'
#         # print('保存文件：',filename)
#         # with open(filename,'w',encoding='utf-8') as file:
#         #     file.write(html)
#         #
#         # 2、数据提取
#         selector = etree.HTML(html)
#         ls = selector.xpath('//li[contains(@class,"j_thread_list clearfix")]')
#         print('len:',len(ls))
#         base_url ='https://tieba.baidu.com'
#         for item in ls:
#             title = item.xpath('.//a[@class ="j_th_tit "]/text()')[0]
#             print('title:',title)
#             detail_url = base_url+item.xpath('.//a[@class ="j_th_tit "]/@href')[0]
#             print('detail url:',detail_url)
#             author = item.xpath('.//span[@class="frs-author-name-wrap"]/a/text()')[0]
#             print('author:',author)
#             nums = item.xpath('.//span[@class="threadlist_rep_num center_text"]/text()')[0]
#             print('nums:',nums)
#             print('='*60)
#             # 3、数据存储
#             #方式一：txt文本文件
#             txtfile = './data/tieba_'+teibaName+'.txt'
#             with open(txtfile,'a',encoding='utf-8') as file:
#                 file.write('title:'+title+',author:'+author+',nums:'+nums+'detail_url:'+detail_url+'\n')
#         sleep(random.random()*2)
# if __name__=='__main__':
#     tiebaName=input('请输入贴吧名称')
#     startPage=int(input('请输入起始页面'))
#     endPage=int(input('请输入结束页面'))
#     tiebaSpider(tiebaName, startPage, endPage)
#
#


import requests  # 网页爬取的请求库
from time import sleep
import random
from lxml import  etree  # 数据提取库
import csv
import codecs

def tiebaSpider(teibarName,startPage,endPage):
    '''
    批量爬取指定贴吧的页面内容
    :param teibarName:
    :param startPage:
    :param endPage:
    :return:
    '''
    url = 'https://tieba.baidu.com/f?'
    headers = {'User-Agent':'Mozilla/5.0 (compatible; WOW64; MSIE 10.0; Windows NT 6.2)'}
    for page in range(startPage,endPage+1):
        # 1、网页爬取
        pn = (page-1) * 50
        params = {
            'kw':tiebaName,
            'pn':pn
        }
        print('爬取页面：',page)
        response  = requests.get(url,params=params,headers=headers)
        html = response.content.decode()
        print(html)
        # filename = './data/第'+str(page)+'页.html'
        # print('保存文件：',filename)
        # with open(filename,'w',encoding='utf-8') as file:
        #     file.write(html)
        #
        # 2、数据提取
        selector = etree.HTML(html)
        ls = selector.xpath('//li[contains(@class,"j_thread_list clearfix")]')
        print('len:',len(ls))
        base_url ='https://tieba.baidu.com'
        for item in ls:
            title = item.xpath('.//a[@class ="j_th_tit "]/text()')[0]
            print('title:',title)
            detail_url = base_url+item.xpath('.//a[@class ="j_th_tit "]/@href')[0]
            print('detail url:',detail_url)
            author = item.xpath('.//span[@class="frs-author-name-wrap"]/a/text()')[0]
            print('author:',author)
            nums = item.xpath('.//span[@class="threadlist_rep_num center_text"]/text()')[0]
            print('nums:',nums)
            print('='*60)
            # 3、数据存储
            #方式一：txt文本文件
            txtfile = './data/tieba_'+teibarName+'.txt'
            with open(txtfile,'a',encoding='utf-8') as file:
                file.write('title:'+title+',author:'+author+',nums:'+nums+'detail_url:'+detail_url+'\n')
            # 方式二：csv格式
            csvfile='./data/tieba_'+teibarName+'.csv'
            with codecs.open(csvfile,'a',encoding='utf-8') as file:
                wr = csv.writer(file)
                wr.writerow([title,author,nums,detail_url])
        sleep(random.random() * 2)

    print('爬取结束')

if __name__ == '__main__':
    tiebaName = input('请求输入贴吧名称：')
    startPage = int(input('请输入起始的页码：'))
    endPage = int(input('请输入结束页码：'))
    tiebaSpider(tiebaName,startPage,endPage)











