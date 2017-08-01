# '''List'''
# shopList = ['Apple','Banana','Carrot','Mango']
# for item in shopList:
#     print item,
#
# print '\n'
# print 'Mine shopList length is',len(shopList)
#
# shopList.append('Rice')
# print shopList
#
# shopList.sort()
# print shopList
#
# print 'The first item i want to buy is',shopList[0]
# doneItem = shopList[0]
# del shopList[0]
# print 'I bought the',doneItem
# print 'Now the shopList is ',shopList
#
#
# '''Tuple'''
# zoo = ('Elephant','Wolf','Penguin')
# print zoo,'zoo length is',len(zoo)
# newZoo = ('Monkey','Dolphin',zoo)
# print newZoo,'newZoo length is',len(newZoo)
#
# print 'Zoo first animal is ',zoo[0]
# print 'Animaals broungth from zoo is',newZoo[2]
# print 'Last animal broungth from zoo is',newZoo[2][2]
#
# name = 'Swaroop'
# age = 22
# print '%s is %d old years' %(name,age)
# print 'Why %s playing with Python' %name
#
#
# '''Dic'''
# dic = {'name':'Jerry',
#        'age':'27',
#        'Country':'China'}
# print dic
#
# dic['gender'] = 'Man'
# print dic
#
# del dic['Country']
# print dic
#
# for name,item in dic.items():
#     print 'key is %s,value is %s' %(name,item)
#
# if 'name' in dic:
#     print '\n name\'s value is %s' %dic['name']


# '''Dequence'''
# shopList = ['Apple','Banana','Pear','Watermelon','Mango']
# print 'shopList 0 item is',shopList[0]
# print 'shopList 0 item is',shopList[-1]
#
# print '0 to 4 item is %s',shopList[0:4]
# print '2 to end item is %s',shopList[2:-1]
# print '2 to end item is %s',shopList[2:]
# print 'start to end item is %s',shopList[:]
#
# name = 'swaroop'
# print 'name 0 to 4 item is ',name[0:4]
# print 'name 1 to end item is ',name[1:-1]
# print 'name 1 to end item is ',name[1:]
# print 'name start to end item is ',name[:]


'''refer & slice'''
shopList = ['Apple','Banana','Pear','Watermelon','Mango']

otherShopList = shopList
print shopList
print  otherShopList

'''copy'''
myShopList = shopList[:]
print 'myShopList is', myShopList
del myShopList[0]
print 'myShopList is', myShopList
print 'shopList is', shopList

name = 'Swaroop'
if name.startswith('Swa'):
    print 'Swaroop start with Swar in front'

if name.find('war') != -1:
    print 'Contain war!'

if 'a' in name:
    print 'Contain ''a'' string'

countryName = ['USA','Canada','Russia','Brazli','France','Gemany','India']
c = '_'
c.join(countryName)
print c.join(countryName)