from lxml import etree

html =etree.parse('hello.html')
print(type(html))     #显示 ertee.parse()返回类型
# 找到所有的li标签
result=html.xpath('//li')
print(result)