#文本进度条
import time


def text_lode(len_s):
    print("开始加载文本".center(len_s, '-'))
    t = time.perf_counter()
    for i in range(len_s+1):
        a = '*' * i
        b = '.' * (len_s-i)
        c = (i/len_s)*100
        t -= time.perf_counter()
        print("\r{:^3.2f}%[{}->{}]{:.2f}s".format(c, a, b, -t), end="")
        time.sleep(0.1)
    print("\n"+"文本加载完成".center(len_s, '-'))


text_lode(5)
