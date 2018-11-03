# 实例一，提高0.001
import math
def progress(factor_p):
    if factor_p >= 0:
        dayUp = math.pow((1.0 + factor_p), 365)
        dayDown = math.pow((1.0 - factor_p), 365)
        # print("天天向上：%s， 向下：%s" % (dayUp, dayDown))
        print("天天向上：{:.2f}， 向下：{:.2f}".format(dayUp, dayDown))
    else:
        print("输入有误，请输入正数")

def improve(factor1, factor2):
    DayUp = 1
    for i in range(365):
        if i % 7 in [6, 0]:
            DayUp = DayUp * (1 - factor1)
        else:
            DayUp = DayUp * (1 + factor2)
    print("向上5天向下2天{:.2f}".format(DayUp))
# progress(0.001)
# progress(0.005)
# progress(0.01)
# progress(-1)

improve(0.01, 0.01)

