def sayHello():
    print 'It\'s a simple function!'

def getMax(a,b):
    if a > b:
        print  a,'is max value'
    else:
        print b,'is max value'

getMax(10,20)
x = 200
y = 280
getMax(x,y)

# '''global'''
# def func():
#     global x
#     print x
#     x = 10
#     print 'local x is changed to',x
#
# x = 2
# func()
# print 'x is',x
#
# def printMessgae(message,times = 1,value = 2):
#     print message * times
#
# printMessgae('Hello')
# printMessgae('Hello',2)
#
#
# def func(a, b=5, c=10):
#     print 'a is', a, 'and b is', b, 'and c is', c
#
# func(3, 7)
# func(25, c=24)
# func(c=50, a=100)

# def getMax(x,y):
#     if x > y:
#         return x
#     elif x < y:
#         return y
#     else:
#         return None
#
# max = getMax(9,9)
# print max
#
# def someFunc():
#     pass
#
# someFunc()


def printMax(x,y):
    '''Print the maximun of the two numbers.

    The two values must be interge'''

    x = int(x)
    y = int(y)
    if x > y:
        print x,'is the maxValue!'
    else:
        print y,'is the maxValue!'

printMax(1,3)
print printMax.__doc__