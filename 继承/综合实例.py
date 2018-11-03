class Dog:
    def __init__(self, name, age=1):
        self.name = name
        self.age = age
    def eat(self):
        print("%s吃饭"%self)
    def play(self):
        print("%s玩" % self)
    def seelp(self):
        print("%s睡觉" % self)
    def watch(self):
        print("%s看家" % self)
    def __str__(self):
        return("名字是{}，年龄{}岁的小狗".format(self.name, self.age))

d = Dog("黑儿", 8)
d.eat()
d.play()