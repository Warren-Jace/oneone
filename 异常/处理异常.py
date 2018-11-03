class Person:
    # eat = 2
    count = 1

# p = Person()
# # print(p.__dict__)
# print(Person.__dict__)
# # del p.eat
# setattr(p, 'eat', 3)
# print(p.__dict__)
# setattr(Person, 'eat', 5)
#
# print(p.eat)
# print(Person.eat)
p = Person()
p.count += 1
print(p.__dict__)
print(Person.__dict__)
x = type()
