# import sys
#
# try:
#     s = raw_input('Enter something -->')
# except EOFError:
#     print 'Get EOFERROR'
#     sys.exit()
# except:
#     print '/n some error/exception occurred.'
# else:
#     print 'Normal back'
#
# print 'Done'

# class ShortInputException(Exception):
#     '''A user-defined exception class.'''
#     def __init__(self, length, atleast):
#         Exception.__init__(self)
#         self.length = length
#         self.atleast = atleast
#
# try:
#     s = raw_input('Enter something --> ')
#     if len(s) < 3:
#         raise ShortInputException(len(s), 3)
#     # Other work can continue as usual here
# except EOFError:
#     print '\nWhy did you do an EOF on me?'
# except ShortInputException, x:
#     print 'ShortInputException: The input was of length %d, \
#           was expecting at least %d' % (x.length, x.atleast)
# else:
#     print 'No exception was raised.'

import time

try:
    f = file('poem.txt')
    while True: # our usual file-reading idiom
        line = f.readline()
        if len(line) == 0:
            break
        time.sleep(2)
        print line,
finally:
    f.close()
    print 'Cleaning up...closed the file'