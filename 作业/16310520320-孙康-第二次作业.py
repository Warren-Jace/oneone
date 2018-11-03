# DayDayUp365
def dayUP(df, factor):
    DayUp = 1
    for i in range(365):
        if i % 7 in [6, 0]:
            DayUp = DayUp * (1 - factor)
        else:
            DayUp = DayUp * (1 + df)
    return DayUp
dayFacotry = 0.01
day_f = 0.02
while(dayUP(dayFacotry, day_f) < 80):
    dayFacotry += 0.001
print("每天的努力参数：{:.2f}".format(dayFacotry))