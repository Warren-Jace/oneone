# 1.打开文件
# r只读的方式打开文件，文件的指针将会安放在文件的开头
# w只写的方式打开文件，文件的指针将会放在文件的开头，所写的新内容会被覆盖，文件不存在时会自动的创建新文件
# a刚打开的时候文件的指针指向文件的末尾，不会覆盖原先的内容，会加在原先内容的后面，文件不存在时，会自动创建一个新文件
# b以二进制操作文件的读写
# f = open("b.txt", "b", encoding='utf-8')
# 2. 读写文件
# content = f.read()
# print(content)
# f.write("1222223")
# f.close()

# f = open("xx.jpg", "rb")#, encoding='utf-8')
# fromfile = f.read()
# print(fromfile)
# f.close()
#
# tofile = open("xx2.jpg", 'wb')
# cc = fromfile[0:len(fromfile)//3]
# tofile.write(cc)
# tofile.close()

# f = open("a.txt", "b+")
# # ff = f.read()
# # print(ff)
# # # f.write("sdfsfsd")
# # # f.write("123")
# # f.close()

# seek指明文件指针的位置，tell打印指针的位置

# whence：可选，默认值为 0。给offset参数一个定义，表示要从哪个位置开始偏移；0代表从文件开头开始算起，1代表从当前位置开始算起，2代表从文件末尾算起。
# f = open("a.txt", "rb")
# print(f.tell())
# # f.seek(2,0)文本文件只能为0
# f.seek(-1,2)
# print(f.tell())
# print(f.read())
# print(f.tell())
# f.close()

f = open("a.txt", "r")
# f.seek(2)
# cc = f.read(2)
# print(f.tell())
# print(cc)
# cc1 = f.readline()
# 打印后不生成换行，直接使用空字符串显示
# print(cc1, end="")
# print("******", f.tell())
# cc1 = f.readline()
# print(cc1, end="")
# print("******", f.tell())
# cc1 = f.readline()
# print(cc1, end="")
# print("******", f.tell())

# 判断文件是否可读取
# if f.readable():
#     cc = f.readlines()
#     for i in cc:
#         print(i, end="")
#
# f.close()

if f.writable():
    print(f.write("asd"))
# 刷新缓冲区
f.flush()

f.close()