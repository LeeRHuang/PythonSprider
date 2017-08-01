# class Person:
#    def __init__(self,name):
#        self.userName = name
#    def sayHi(self):
#        print 'How are you?',self.userName
#
# p = Person('Swaroop')
# p.sayHi()


# class person:
#     population = 0
#
#     def __init__(self,name):
#         self.name = name
#         print 'Initlializes is %s.' % self.name
#         person.population += 1
#
#     def __del__(self):
#         print '%s say bye' % self.name
#         person.population -= 1
#         if person.population == 0:
#             print 'i am the last one.'
#         else:
#             print 'there is still %d people here.' % person.population
#
#     def sayHi(self):
#         print 'Hi,my name is %s.' % self.name
#
#
#     def howMany(self):
#         if person.population == 1:
#             print 'i am the only people here.'
#         else:
#             print 'we have %d people here.' % person.population
#
#
# firstPerson = person('Lucy')
# firstPerson.sayHi()
# firstPerson.howMany()

# secondPerson = person('Jone')
# secondPerson.sayHi()
# secondPerson.howMany()
#
# del firstPerson
# del secondPerson
# #
# firstPerson.sayHi()
# firstPerson.howMany()


class SchoolMember:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def tell(self):
        print 'name is %s ,age is %s' %(self.name,self.age)

class Techer(SchoolMember):
    def __init__(self,name,age,salary):
        SchoolMember.__init__(self,name,age)
        self.salary = salary
    def tell(self):
        print 'salary is %s ' %self.salary

class Student(SchoolMember):
    def __init__(self,name,age,mark):
        SchoolMember.__init__(self,name,age)
        self.mark = mark

    def tell(self):
        print 'mark is %s ' %self.mark


t = Techer('Molly','30','200000')
t.tell()

s = Student('Tom','15','89')
s.tell()