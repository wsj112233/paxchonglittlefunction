#!/user/bin/env python
# -*- coding: utf-8 -*-

fpath='E:\python\charmpythonproject\爬虫\英雄联盟专题\lolinfo.txt'
with open(fpath,'r',encoding='utf-8') as f:
    for line in f:
        line_str=eval(line)
        print(line_str['英雄名称:'])

name=input('请输入所需要查询英雄名称:')
with open(fpath,'r',encoding='utf-8') as f1:
    for line1 in f1:
        line_str1=eval(line1)

        if name==line_str1['英雄名称:']:
            print(line_str1)

        else:
            continue



