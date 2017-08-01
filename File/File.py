# poem = '''\
# Programming is fun
# When the work is done
# if you wanna make your work also fun:
#         use Python!
# '''
#
# f = file('poem.txt','w')
# f.write(poem)
# f.close()
#
# f = file('poem.txt')
# while True:
#     line = f.readline()
#     if len(line) == 0:
#         break
#     print line,
# f.close()

#
# import cPickle as p
#
# shoplistfile = 'shoplist.data'
# shoplist = ['apple','lemone','pear']
# f = file(shoplistfile,'w')
# p.dump(shoplist,f)
# f.close()
#
# del shoplist
#
# f = file(shoplistfile,'r')
# storelist = p.load(f)
# print storelist
