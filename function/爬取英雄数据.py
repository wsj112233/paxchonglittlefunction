#!/user/bin/env python
# -*- coding: utf-8 -*-

import requests,traceback
from bs4 import BeautifulSoup

def getHTMLText(url):
    try:
        r=requests.get(url,timeout=30)
        r.raise_for_status()
        r.encoding=r.apparent_encoding
        return r.text
    except:
        ""

def getherolist(lst,hero_url):
    html=getHTMLText(hero_url)
    soup=BeautifulSoup(html,'html.parser')
    ul = soup.find('ul', attrs={'id': 'champion_list'})  # <class 'bs4.element.Tag'>
    a=ul.find_all('a')
    for i in a:
        try:
            href=i.attrs['href']
            lst.append(href)

        except:
            continue


def getheroinfo(lst,fpath):
    for url_new in lst:
        url_hero=url_new
        html=getHTMLText(url_hero)
        try:
            if html=="":
                continue
            else:
                infoDisk={}
                """
                先爬取每个英雄的名称
                """
                soup_hero=BeautifulSoup(html,'html.parser')
                heroname_div=soup_hero.find('div',attrs={'class':'mod-crumbs'})
                heroname_b=heroname_div.find_all('b')[0]
                heroname=heroname_b.string
                infoDisk['英雄名称:']=heroname


                """
                对每个英雄的属性进行爬取
                放入infoDict字典里
                """
                herobox_div = soup_hero.find('div', attrs={'class': 'hero-box ext-attr'})  # Tag类型
                keylist=herobox_div.find_all('em')       #list类型
                valuelist=herobox_div.find_all('span')
                for i in range(len(keylist)):
                    key=keylist[i].string
                    value=valuelist[i].string
                    infoDisk[key]=value

                """
                将本条爬取记录文本txt：fpath中
                """
                with open(fpath,'a',encoding='utf-8') as f:
                    f.write(str(infoDisk)+'\n')

        except:
            traceback.print_exc()
            continue



def main():
    hero_url='http://lol.duowan.com/hero/'
    output_file='E:\python\charmpythonproject\爬虫\英雄联盟专题\lolinfo.txt'
    slist=[]
    getherolist(slist,hero_url)
    getheroinfo(slist,output_file)

main()



