# def jia(n1, n2):
#     return n1 + n2
# def jian(n1, n2):
#     return n1 - n2
# def cheng(n1, n2):
#     return n1 * n2
# def chu(n1, n2):
#     return n1 / n2
#
# r1 = jia(2, 6)
# r2 = jian(1, 4)
# r3 = cheng(2, 5)

# class caculator:
#     __result = 0
#     @classmethod
#     def first(cla, v):
#         # global result
#         cla.__result = v
#
#     @classmethod
#     def jia(cls, n):
#         # global result
#         cls.__result += n
#         # return n1 + n2
#
#     @classmethod
#     def jian(cls, n):
#         # global result
#         cls.__result -= n
#         # return n1 - n2
#
#     @classmethod
#     def cheng(cls, n):
#         # global result
#         cls.__result *= n
#         # return n1 * n2
#
#     @classmethod
#     def chu(cls, n):
#         global __result
#         cls.__result /= n
#         # return n1 / n2
#
#     @classmethod
#     def show(cls):
#         print(cls.__result)

# first(2)
# jia(6)
# jian(4)
# cheng(5)
# print(result)

# class caculator:
#     __result = 0
#     def __init__(self, num):
#         self.__result = num
#
#     def jia(self, n):
#         self.__result += n
#
#     def jian(self, n):
#         self.__result -= n
#
#     def cheng(self, n):
#
#         self.__result *= n
#
#     def chu(self, n):
#         self.__result /= n
#
#     def show(self):
#         print(self.__result)


# class caculator:
#     def check_num(self,num):
#         if not isinstance(num, int):
#             raise TypeError("出错")
#     def __init__(self, num):
#         self.check_num(num)
#         self.__result = num
#
#     def jia(self, n):
#         self.check_num(num)
#         self.__result += n
#
#     def jian(self, n):
#         self.check_num(num)
#         self.__result -= n
#
#     def cheng(self, n):
#         self.check_num(num)
#         self.__result *= n
#
#     def chu(self, n):
#         self.check_num(num)
#         self.__result /= n
#
#     def show(self):
#         print(self.__result)


# class caculator:
#     def check_num_zsq(func):
#         def inner(self, n):
#             if not isinstance(num, int):
#                 raise TypeError("出错")
#             return func(self, n)
#         return inner
#
#     @check_num_zsq
#     def __init__(self, num):
#
#         self.__result = num
#
#     @check_num_zsq
#     def jia(self, n):
#
#         self.__result += n
#
#     @check_num_zsq
#     def jian(self, n):
#
#         self.__result -= n
#
#     @check_num_zsq
#     def cheng(self, n):
#
#         self.__result *= n
#
#     @check_num_zsq
#     def chu(self, n):
#
#         self.__result /= n
#
#     def show(self):
#         print(self.__result)

import win32com.client
speaker = win32com.client.D
class caculator:
    def __check_num_zsq(func):
        def inner(self, n):
            if not isinstance(num, int):
                raise TypeError("出错")
            return func(self, n)
        return inner

    @__check_num_zsq
    def __init__(self, num):

        self.__result = num

    @__check_num_zsq
    def jia(self, n):

        self.__result += n

    @__check_num_zsq
    def jian(self, n):

        self.__result -= n

    @__check_num_zsq
    def cheng(self, n):

        self.__result *= n

    @__check_num_zsq
    def chu(self, n):

        self.__result /= n

    def show(self):
        print(self.__result)