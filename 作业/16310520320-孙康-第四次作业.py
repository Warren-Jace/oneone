#计算圆周率PI
import random
import math
import time
F = 100000
count_r = 0
time.perf_counter()
for i in range(1, F+1):
    x, y = random.random(), random.random()
    dist = math.sqrt(x ** 2 + y ** 2)
    if dist <= 1.0:
        count_r += 1
pi = 4 * (count_r/F)
print("PI值是{}".format(pi))
print("运行时间是：{:5.6}s".format(time.perf_counter()))