# -*- coding: utf-8 -*-
"""
   File Name：     04-Beautiful_Soup
   Description :
   date：          2020/2/11
"""
# https://cuiqingcai.com/5548.html
from bs4 import BeautifulSoup
import re

# soup = BeautifulSoup('<p>hello<p>', 'lxml')
# print(soup.p.string)


# html = """
# <html><head><title>The Dormouse's story</title></head>
# <body>
# <p class="title" name="dromouse"><b>The Dormouse's story</b></p>
# <p class="story">Once upon a time there were three little sisters; and their names were
# <a href="http://example.com/elsie" class="sister" id="link1"><!-- Elsie --></a>,
# <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
# <a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
# and they lived at the bottom of a well.</p>
# <p class="story">...</p>
# """
# soup = BeautifulSoup(html, 'lxml')
# print(soup.prettify())
# print(soup.title.string)
# print(type(soup.title))
# print(soup.head)
# print(soup.p)
# print(soup.title.name)
# print(soup.p.attrs)
# print(soup.p.attrs['name'])
# print(soup.p['name'])
# print(soup.p['class'])

html = '''
<div class="panel">
    <div class="panel-heading">
        <h4>Hello</h4>
    </div>
    <div class="panel-body">
        <ul class="list" id="list-1">
            <li class="element">Foo</li>
            <li class="element">Bar</li>
            <li class="element">Jay</li>
        </ul>
        <ul class="list list-small" id="list-2">
            <li class="element">Foo</li>
            <li class="element">Bar</li>
        </ul>
    </div>
</div>
'''
soup = BeautifulSoup(html, 'lxml')
# print(soup.find_all(name='ul'))
# print(type(soup.find_all(name='ul')[0]))
# for ul in soup.find_all(name='ul'):
#     print(ul.find_all(name='li'))
#     for li in ul.find_all(name='li'):
#         print(li.string)

# print(soup.find_all(attrs={'id': 'list-1'}))
# print(soup.find_all(attrs={'class': 'element'}))


# print(soup.find_all(id='list-1'))
# print(soup.find_all(class_='element'))

# html = '''
# <div class="panel">
#     <div class="panel-body">
#         <a>Hello, this is a link</a>
#         <a>Hello, this is a link, too</a>
#     </div>
# </div>
# '''
# soup = BeautifulSoup(html, 'lxml')
# print(soup.find_all(text=re.compile('link')))

# CSS选择器
html='''
<div class="panel">
    <div class="panel-heading">
        <h4>Hello</h4>
    </div>
    <div class="panel-body">
        <ul class="list" id="list-1">
            <li class="element">Foo</li>
            <li class="element">Bar</li>
            <li class="element">Jay</li>
        </ul>
        <ul class="list list-small" id="list-2">
            <li class="element">Foo</li>
            <li class="element">Bar</li>
        </ul>
    </div>
</div>
'''
soup = BeautifulSoup(html, 'lxml')
print(soup.select('.panel .panel-heading'))
print(soup.select('ul li'))
print(soup.select('#list-2 .element'))
print(type(soup.select('ul')[0]))
