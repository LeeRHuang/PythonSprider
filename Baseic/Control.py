'''if'''
# number = 23
# guess = int(raw_input('Please enter an integer : '))
#
# if guess == number:
#     print 'Congratulations you got it!'
#     print 'Now you can get a amount of money'
# elif guess > number:
#     print 'Sorry the number is a litter higher than you input,you have to try again'
# elif guess < number:
#     print 'Sorry the number is a litter lower than you input,you have to try again'
# else:
#     print 'Done'

''''while'''
# number = 23
# running = True
#
# while running:
#     guess = int(raw_input("Please enter an integer : "))
#     if guess == number:
#         print 'You got it!'
#         running = False
#     elif guess > number:
#
#         print 'More Higher than guess'
#     elif guess < number:
#
#         print 'Litter lower than that guess'
#
# else:
#     print 'While loop over!'
#
# print 'Done'

'''for'''
# for i in range(1,10):
#     print  i
#     if i == 2:
#         break
# else:
#     print 'Loop is over!'
#
# for j in range(1,10,8):
#     print j

'''break'''
# flag = True
# while flag:
#     s = raw_input('Please input some words : ')
#     if s == 'quit':
#         flag = False
#         break
#     print 's\'s length is',len(s)
# else:
#     print 'Sorry,please input again'
# print 'Done'


'''contuine'''
# flag = True
# while flag:
#     s = raw_input('Please input some keyWords : ')
#     if s == 'quit':
#         print 'That\'s right'
#         flag = False
#         break
#     if len(s) < 3:
#         print 'contuine'
#         continue
#     print 'Input is of sufficient length'