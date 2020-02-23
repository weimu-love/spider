# -*- coding: utf-8 -*-
"""
   File Name：     03-Xpath
   Description :
   date：          2020/2/11
"""
from lxml import etree

text = '''
<div>
    <ul>
         <li class="item-0"><a href="link1.html">first item</a></li>
         <li class="item-1"><a href="link2.html">second item</a></li>
         <li class="item-inactive"><a href="link3.html">third item</a></li>
         <li class="item-1"><a href="link4.html">fourth item</a></li>
         <li class="item-0"><a href="link5.html">fifth item</a>
     </ul>
 </div>
'''
html = etree.HTML(text)
# result = etree.tostring(html)
# print(result.decode('utf-8'))


# result = html.xpath('//li[@class="item-0"]/text()')
# print(result)


# result = html.xpath('//li[@class="item-0"]/a/text()')
# print(result)


# result = html.xpath('//li/a/@href')
# print(result)


# 属性多值匹配
# text = '''
# <li class="li li-first"><a href="link.html">first item</a></li>
# '''
# html = etree.HTML(text)
# # result = html.xpath('//li[@class="li"]/a/text()')
# result = html.xpath('//li[contains(@class,"li")]/a/text()')
# print(result)


# 多属性匹配
# text = '''
# <li class="li li-first" name="item"><a href="link.html">first item</a></li>
# '''
# html = etree.HTML(text)
# result = html.xpath('//li[contains(@class,"li") and @name="item"]/a/text()')
# print(result)

# 按序选择
# html = etree.HTML(text)
# result = html.xpath('//li[1]/a/text()')
# print(result)
# result = html.xpath('//li[last()]/a/text()')
# print(result)
# result = html.xpath('//li[position()<3]/a/text()')
# print(result)
# result = html.xpath('//li[last()-2]/a/text()')
# print(result)


# 节点轴选择
html = etree.HTML(text)
# 第一个li节点的所有祖先节点，包括html、body、div和ul
result = html.xpath('//li[1]/ancestor::*')
print(result)

result = html.xpath('//li[1]/ancestor::div')
print(result)
# 可以获取所有属性值，其后跟的选择器还是*，这代表获取节点的所有属性，返回值就是li节点的所有属性值
result = html.xpath('//li[1]/attribute::*')
print(result)
result = html.xpath('//li[1]/child::a[@href="link1.html"]')
print(result)
# 我们调用了descendant轴，可以获取所有子孙节点。这里我们又加了限定条件获取span节点，所以返回的结果只包含span节点而不包含a节点
result = html.xpath('//li[1]/descendant::span')
print(result)
# 可以获取当前节点之后的所有节点。这里我们虽然使用的是*匹配，但又加了索引选择，所以只获取了第二个后续节点
result = html.xpath('//li[1]/following::*[2]')
print(result)
# 可以获取当前节点之后的所有同级节点。这里我们使用*匹配，所以获取了所有后续同级节点
result = html.xpath('//li[1]/following-sibling::*')
print(result)
