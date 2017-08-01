import sys
#
# print 'The Commond line arguments are:'
# for i in sys.argv:
#     print i
# print '\n the path is ',sys.path,'\n'
#
# if __name__ == '__main__':
#     print 'the program running by it self!'
# else:
#     print 'i am being import from other module'

path = dir(sys)
print 'path is',path
print '\n'
path = dir()
print 'path is',path

a = 10
path = dir()
print 'path is',path

del  a
path = dir()
print 'path is',path
print __name__

