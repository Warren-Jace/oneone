temp = input("输入需要转换的温度：")
while temp not in ['n', 'N']:
    if temp[-1] in ['f', 'F']:
        C = (eval(temp[0:-1])-32)/1.8
        print("转换后的温度是：{:.2f}C".format(C))
    elif temp[-1] in ['c', 'C']:
        F = eval(temp[0:-1])*1.8+32
        print("转换后的温度是：{:.2f}F".format(F))
    else:
        print("输入有误")
    temp = input("输入需要转换的温度(结束为n或N)：")
print("结束输入!")