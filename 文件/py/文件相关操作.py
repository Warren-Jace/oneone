# import os
# # os.rename("a.txt", "aa.txt")
# print(os.getcwd())
# print(os.listdir("./"))

# source_file = open("aa.txt", "r")
# dst_file = open("bb.txt", "a")
#
# while True:
#     content = source_file.read(7)
#     if len(content) == 0:
#         break;
#     print(content)
#     dst_file.write(content)
# source_file.close()
# dst_file.close()

# import os
# import shutil
#
# path = "./"
# if not os.path.exists(path):
#     exit()
# os.chdir("path")
# file_list = os.listdir("./")
# # print(file_list)
# for file_name in file_list:
#     # print(file_name)
#     # 查找索引位置
#     index = file_name.rfind(".")
#     if index == -1:
#         print(index)
#
#         continue
#     # print(index)
#     extension = file_name[index + 1:]
#     print(extension)
#     if not os.path.exists(extension):
#        os.mkdir(extension)
#
#     shutil.move(file_name, extension)

# import os
# os.chdir("../")
# os.chdir("../")
#
#
# def listFiles(dir, file):
#     file_list = os.listdir(dir)
#     for file_name in file_list:
#         New_FileName = dir + "/" + file_name
#         if os.path.isdir(New_FileName):
#             # print(New_FileName)
#             file.write(New_FileName)
#             listFiles(New_FileName)
#         else:
#             print("\t" + file_name)
#     print("")
#
#
# f = open("list.txt", "a")
# listFiles("文件", f)


import os
os.chdir("../")
os.chdir("../")


def ListFiles(dir, file):
    file_list = os.listdir(dir)
    for file_name in file_list:
        New_FileName = dir + "/" + file_name
        if os.path.isdir(New_FileName):
            # print(New_FileName)
            file.write(New_FileName + "\n")
            ListFiles(New_FileName, file)
        else:
            # print("\t" + file_name)
            file.write("\t" + file_name + "\n")

    # print("")
    file.write("\n")


f = open("list.txt", "a")
ListFiles("文件", f)
