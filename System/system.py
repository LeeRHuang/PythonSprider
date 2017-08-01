# coding=utf-8
# import sys
# def readfile(filename):
#     f = file(filename)
#     while True:
#         readline = f.readline()
#         if len(readline) == 0:
#             break
#         print readline,
#     f.close()
#
# #Script start from here
# if len(sys.argv) < 2:
#     print 'No action specified.'
#     sys.exit()
#
# arg = sys.argv[1]
# print 'arg is %s' %arg
# if arg.startswith('--'):
#     # 从第3个字符开始切割直到结尾
#     option = arg[2:]
#     if option == 'version':
#         print 'version 1.2'
#     elif option == 'help':
#         print '''This program prints files to the standard output.
#                  Any number of files can be specified.
#                  Options include:
#                  --version : Prints the version number
#                  --help    : Display this help'''
#     else:
#         print 'Unknow exception'
#     sys.exit()
# else:
#     for filename in sys.argv[1:]:
#         print 'filename is %s' %filename
#         readfile(filename)

# list = [1,2,3,4]
# listDoubel = [2*i for i in list]
# listThree = list*3
#
# print list
# print listDoubel
# print listThree
#
# def powerSum(power,*arg):
#     total = 0
#     for i in arg:
#         total += pow(i,power) #x的y次方
#     return total
#
# # total = powerSum(2,3,4)
# total = powerSum(2,3)
# print total
#
# def findad(username, **args):
#     '''''find address by dictionary'''
#     print 'Hello: ', username
#     for name, address in args.items():
#         i = args[name]
#         print i
#         print 'Contact %s at %s' % (name, address)
# findad('wcdj', gerry='gerry@byteofpython.info',
#         wcdj='wcdj@126.com', yj='yj@gmail.com')
#
# def getName(username,**args):
#
#     print 'Hello: ', username
#     for key,value in args.items():
#         print 'key is %s,value is %s' %(key,value)
#
# getName('Lee',Email = 'lirihuang@126.com',Mobile = '18910898751',Gender = 'M')

# def make_Repter(n):
#     return lambda s: s*n
#
# twice = make_Repter(6)
# print twice
# print twice('Go')
# print twice(6)
#
# foo = [1,10,30,43,59,8]
# f = filter(lambda x: x % 3 == 0,foo)
# f1 = [i for i in foo if i % 3 == 0]
# print(f)
# print(f1)
#
# m = map(lambda x: x*2 + 10,foo)
# m1 = [i*2 + 10 for i in foo]
# print m
# print m1
#
# r = reduce(lambda x,y: x + y,foo)
# print r
#
# exec 'print "Hello world"'
# eval('2*3')
#
# list = ['item']
# print list
# assert len(list) >= 1
# list.pop()
#
# print list
#
# a = 'Hello world'
# b = str(a)
# c = eval(repr(a))
#
# print a
# print b
# print c
#
# print str(a)
# print repr(a)
#
# i = []
# i.append('item')
# print i
# print repr(i)



