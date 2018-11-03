# class Money:
#     pass
# Money是引用class中的Money
# Money = 666
# one = Money
# print(one)
# print(Money)
class person:
    pass

# p = person()
# p1 = person()
#
# # p.age = 18
# # print(p.sex)
# # print(p.__dict__)
# # p.pets = ["xiaohua", "xiaohei"]
# # print(p.pets, id(p.pets))
# # p.pets = [1, 2]
# # print(p.pets, id(p.pets))
# #
# # p.pets.append("xiaohuang")
# # print(p.pets, id(p.pets))
#
# # del p.age
# # print(p.age)
#
# p.age =18
# p1.address = "shanghai"
#
# print(p1.age)

# person.age = 18
# print(person.age)
# print(person.__dict__)


class Money:
    age = 18
    count = 4
    num = 666
# print(Money.__dict__)
# one = Money()
# print(one.__class__)

Money.age = 22
print(Money.age)