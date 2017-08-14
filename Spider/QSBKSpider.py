# -*- coding: utf-8 -*-
import os
import re
import urllib2
from bs4 import BeautifulSoup

class QSBK:

   def sprider(self):
       i = 1 #定义一个索引变量
       soup = getSoup() #初始化网页解析库实例
       f = fileHandler() #初始化文件
       getContent(soup,f,i) #解析获取内容


def loadData():
    url = 'https://www.qiushibaike.com/' #其实百科首页地址
    user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)' #UA
    headers = {'User-Agent': user_agent}
    req = urllib2.Request(url, headers=headers) #头部添加UA
    response = urllib2.urlopen(req) #发起请求
    return response


def getSoup():
    response = loadData()
    html = response.read().decode('utf-8') #获取网页内容
    soup = BeautifulSoup(html, 'lxml') #通过美丽鸡汤以xml形势解析
    return soup


def fileHandler():
    foldPath = u'糗事百科'
    if not os.path.exists(foldPath):
        os.mkdir(foldPath)
    path = foldPath + '/' + 'QSBK.txt'
    f = file(path, 'w')
    return f


def writeData(c,f,i):
    f.write('第%s条' % i)
    f.write(c.encode('utf8'))
    f.write('\n')


def getContent(soup,f,i):
    article = soup.find_all(class_=re.compile("article block untagged")) #通过article block untagged标签解析tag节点
    for item in article:
        username = item.h2.get_text() #获取用户昵称
        img = item.img['src'] #获取头像
        contents = item.select('.content') #获取内容tag节点
        content = contents[0].span.get_text() #
        number = item.select('.number') #获取number列表
        vote = number[0].get_text() #点赞数
        comment = number[1].get_text() #评论数

        c = u"昵称:%s内容:%s点赞数:%s\n评论数:%s '\n' " %(username,content,vote,comment)
        writeData(c, f, i) #写入文件
        i += 1
    f.close()


#主程序入口
if __name__ == '__main__':
    qsbk = QSBK()
    qsbk.sprider()