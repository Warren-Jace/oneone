#身体质量指数BMI
height, weight = eval(input("请输入身高（m）和体重(kg)[逗号分隔]:"))
bmi = weight / pow(height, 2)
print("BMI数值为：{:.2f}".format(bmi))
inter, counter = "肥胖", "肥胖"
if bmi < 18.5:
    inter, counter = "偏瘦", "偏瘦"
elif 18.5 <= bmi < 24:
    inter, counter = "正常", "正常"
elif 24 <= bmi < 25:
    inter, counter = "正常", "偏胖"
elif 25 <= bmi < 28:
    inter, counter = "偏胖", "偏胖"
elif 28 <= bmi < 30:
    inter, counter = "偏胖", "肥胖"
print("BMI国际指标{}，国内指标{}".format(inter, counter))