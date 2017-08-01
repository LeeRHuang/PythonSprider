# -*- coding: utf-8 -*-
import urllib2,os
import cookielib

def spiderBaidu():
    try:
        request = urllib2.Request("http://www.baidu.com")
        res = urllib2.urlopen(request)
        info = res.info()
        realUrl = res.geturl()
        print 'real url is ',realUrl
        print 'info is ',info
        html = res.read()
        path = u'百度首页'
        if not os.path.exists(path):
            os.mkdir(path)
        filename = path + '/' + 'baidu.html'
        f = file(filename, 'w')
        f.write(html)
        f.close()
    except urllib2.HTTPError,e:
        print 'error code is ',e.code
    except urllib2.URLError,e:
        print 'error reason is ',e.reason
    else:
        print 'No exception was rasied'


def hander():
    # 创建一个密码管理者
    password_mgr = urllib2.HTTPPasswordMgrWithDefaultRealm()

    # 添加用户名和密码

    top_level_url = "http://example.com/foo/"

    # 如果知道 realm, 我们可以使用他代替 ``None``.
    # password_mgr.add_password(None, top_level_url, username, password)
    password_mgr.add_password(None, top_level_url, 'why', '1223')

    # 创建了一个新的handler
    handler = urllib2.HTTPBasicAuthHandler(password_mgr)

    # 创建 "opener" (OpenerDirector 实例)
    opener = urllib2.build_opener(handler)

    a_url = 'http://www.baidu.com/'

    # 使用 opener 获取一个URL
    opener.open(a_url)

    # 安装 opener.
    # 现在所有调用 urllib2.urlopen 将用我们的 opener.
    urllib2.install_opener(opener)


def handleCookie():
    cookie = cookielib.CookieJar()
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
    res = opener.open('http://www.baidu.com')
    for item in cookie:
        print 'Name = '+ item.name
        print 'Value = '+ item.value


def debugLog():
    httpLog = urllib2.HTTPHandler(debuglevel=1)
    httpsLog = urllib2.HTTPSHandler(debuglevel=1)
    opener = urllib2.build_opener(httpLog,httpsLog)
    urllib2.install_opener(opener)
    res = urllib2.urlopen('http://www.baidu.com')

if __name__ == '__main__':
    spiderBaidu()
    # hander()
    # handleCookie()
    # debugLog()