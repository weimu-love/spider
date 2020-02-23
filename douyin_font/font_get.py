# -*- coding: utf-8 -*-
"""
   File Name：     font_get
   Description :
   date：          2020/2/23
"""
import re
import requests
from lxml import etree

start_url = 'https://www.iesdouyin.com/share/user/88445518961'


def get_real_num(content):
    content = content.replace(' &#', '0').replace('; ', '')
    regex_list = [
        {'name': ['0xe602', '0xe60e', '0xe618'], 'value': '1'},
        {'name': ['0xe603', '0xe60d', '0xe616'], 'value': '0'},
        {'name': ['0xe604', '0xe611', '0xe61a'], 'value': '3'},
        {'name': ['0xe605', '0xe610', '0xe617'], 'value': '2'},
        {'name': ['0xe606', '0xe60c', '0xe619'], 'value': '4'},
        {'name': ['0xe607', '0xe60f', '0xe61b'], 'value': '5'},
        {'name': ['0xe608', '0xe612', '0xe61f'], 'value': '6'},
        {'name': ['0xe609', '0xe615', '0xe61e'], 'value': '9'},
        {'name': ['0xe60a', '0xe613', '0xe61c'], 'value': '7'},
        {'name': ['0xe60b', '0xe614', '0xe61d'], 'value': '8'}
    ]

    for i1 in regex_list:
        for font_code in i1['name']:
            content = re.sub(font_code, str(i1['value']), content)

    # print(content)

    html = etree.HTML(content)
    douyin_info = {}

    # 获取抖音ID
    douyin_id = ''.join(html.xpath("//div[@class='personal-card']/div[@class='info1']//p[@class='shortid']//text()"))
    douyin_id = douyin_id.replace('抖音ID：', '').replace(' ', '')

    # 获取关注量，粉丝数,获赞数
    nums = ''.join(html.xpath(
        "//div[@class='personal-card']/div[@class='info2']//p[@class='follow-info']//span[@class='num']//text()"))
    nums = [i for i in nums.split() if i != ' ']
    focus_nums, fensi, good = nums[0], nums[1], nums[2]
    # print(focus_nums, fensi, good)

    # 获取作品数,喜欢数
    write_like = ''.join(html.xpath("//div[@class='video-tab']/div[@class='tab-wrap']//span[@class='num']//text()"))
    write_like = [i for i in write_like.split() if i != ' ']
    writes, likes = write_like[0], write_like[1]
    # print(writes, likes)

    douyin_info['douyin_id'] = douyin_id
    douyin_info['focus_nums'] = focus_nums
    douyin_info['fensi'] = fensi
    douyin_info['good'] = good
    douyin_info['writes'] = writes
    douyin_info['likes'] = likes

    return douyin_info


def get_html():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36',
    }
    response = requests.get(url=start_url, headers=headers, verify=False)
    return response.text


def run():
    content = get_html()
    info = get_real_num(content)
    print(info)


if __name__ == '__main__':
    run()
