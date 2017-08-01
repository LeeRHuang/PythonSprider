#!/usr/bin/python
#coding:utf-8
import os
import time

# source = ['/Users/rihuangli/Desktop/技术调研/CoreML.md', '/Users/rihuangli/Desktop/技术调研/Swift混编.md']
# target_dir = '/Users/rihuangli/Desktop/技术调研/BackUp/'
#
# target = target_dir + time.strftime('%Y%m%d%H%M%S') + '.zip'
# zip_command = "zip -qr '%s' %s" %(target, ' '.join(source))
#
# if os.system(zip_command) ==0:
#     print 'Success backUp to',target
# else:
#     print 'Fail backUp file'

source = ['/Users/rihuangli/Desktop/技术调研/CoreML.md', '/Users/rihuangli/Desktop/技术调研/Swift混编.md']
target_dir = '/Users/rihuangli/Desktop/技术调研/BackUp/'

today = target_dir + time.strftime('%Y-%m-%d')
now = time.strftime('%H:%M:%S')

comment = raw_input('Please input dir: ')
if len(comment) == 0:
    target = today + os.sep + now + '.zip'
else:
    target = today + os.sep + now + '_' + comment.replace(' ','_') + '.zip'

if not os.path.exists(today):
    os.mkdir(today)
    print 'Successful creat today director! %s',today

zip_command = "zip -qr '%s' %s" %(target,' '.join(source))

if os.system(zip_command) == 0:
    print 'Successful backup to %s', target
else:
    print 'Fail backUp file'



