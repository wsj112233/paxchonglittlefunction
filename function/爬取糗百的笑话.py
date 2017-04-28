#!/user/bin/env python
# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup


def getHTMLText(url):
    try:
        r=requests.get(url,timeout=30)
        r.raise_for_status()
        r.encoding=r.apparent_encoding
        html=r.text
        return html

    except:
        print('异常')


def loadpage(url1,page):
    url=url1+str(page)
    html=getHTMLText(url)
    #开始做汤
    soup=BeautifulSoup(html,'html.parser')
    div=soup.find_all('div',attrs={'class':'article block untagged mb15'})
    storylist=[]
    for i in div:
        storyDict={}
        jpg=i.find_all('div',attrs={'class':'thumb'})
        if jpg !=[]:           #有图片这个属性字段，则跳过不显示
            continue
        h2=i.find_all('h2')[0]
        name=h2.string                          #发布人姓名
        storyDict['发布者']=name

        div_content=i.find_all('div',attrs={'class':'content'})[0]
        content_Tag=div_content.find('span')
        content_text=content_Tag.text       #笑话内容
        storyDict['笑话内容']=content_text

        div_stats=i.find_all('div',attrs={'class':'stats'})[0]
        i=div_stats.find('i',attrs={'class':'number'})
        i1=i.string                         #点赞数
        storyDict['点赞数']=i1
        storylist.append(storyDict)
    return storylist                #将一个笑话的所有信息放在字典里然后追加到list中

def printstory(storylist,page):
    print('********当前第'+str(page)+'页***********')      #打印当前页数
    print('-------------------------------')
    #count=1
    for items in storylist:
        name=items['发布者']
        content=items['笑话内容']
        prize=items['点赞数']
        loadstory(name,content,prize)
        # print('发布者'+name)
        # print(content)
        # print('点赞数'+prize)
        # print('===============================')
    page=page+1
    return page


def loadstory(name,content,prize):
    a=input('按回车输出下一个段子，按q健结束：')
    if a=='q':
        exit(0)

    print('===============================')
    print('发布者'+name)
    print(content)
    print('点赞数'+prize)
    print('===============================')


page=1
url1='http://www.qiushibaike.com/hot/page/'
while True:
    storylist=loadpage(url1,page)
    page=printstory(storylist,page)

