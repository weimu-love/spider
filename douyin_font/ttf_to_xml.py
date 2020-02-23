# -*- coding: utf-8 -*-
"""
   File Name：     font
   Description :
   date：          2020/2/23
"""
from fontTools.ttLib import TTFont

font_1 = TTFont('douyin.ttf')
font_1.saveXML('font_1.xml')
