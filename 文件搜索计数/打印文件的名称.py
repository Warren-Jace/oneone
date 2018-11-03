#遍历文件名
# 传统的遍历文件的方法
# import os, os.path
# def func(arg, dirname, names):
#     for filespath in names:
#         print (os.path.join(dirname, filespath))
#
# index = 1
# for root, subdirs, files in os.walk("D:\学习\大三\python\Python_pyCharm_ll\文件搜索计数"):
#     print(index)
#     index += 1
#     for filepath in files:
#         print(os.path.join(filepath))
#     for sub in subdirs:
#         print(os.path.join(sub))
#
# print("-"*30)
# g = os.walk("D:\学习\大三\python\Python_pyCharm_ll")
# print(g.__next__())
# print(g.__next__())
#
# from pathlib import Path
# p = Path("D:\学习\大三\python\Python_pyCharm_ll")
# print(p)
# print(p.parent)
# print(p.parents)
# print(p.iterdir().__next__())
# print(p.match('D:D:\学习\大三\python'))
# print(p.glob('.py'))

# import os
# from pathlib import Path
# def file_count(path):
#     index = 1
#     p = Path(path)
#
#     for root, subDir, files in os.walk(p):
#         print("第{:-^30}层".format(index))
#         index += 1
#         file_number = 0
#         for sub in subDir:
#             file_number += 1
#             # print(sub)
#         if file_number > 0:
#             print(subDir, '目录下的文件个数：', file_number)
#         file_n = 0
#         for file in files:
#             file_n += 1
#             # print(file)
#         print(root, '目录下的文件个数：', file_n)
#
#
# p = Path("D:\学习\大三\python\Python_pyCharm_ll")
# file_count(p)


# import os
# from pathlib import Path
# index = 1
# p = Path("D:\学习\大三\python\Python_pyCharm_ll")
#
# for root, subDir, files in os.walk(p):
#     print("第{:-^30}层".format(index))
#     index += 1
#     file_number = 0
#     # print(len(subDir))
#     for sub in subDir:
#         file_number += 1
#         # print(sub)
#     if file_number > 0:
#         print(subDir, '目录下的文件个数：', file_number)
#     file_n = 0
#     for file in files:
#         file_n += 1
#         # print(file)
#     print(root, '目录下的文件个数：', file_n)
#
# # print(len(subDir))






