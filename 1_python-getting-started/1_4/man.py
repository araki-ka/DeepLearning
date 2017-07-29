# 1.4.2 クラス
class Man:
    def __init__(self, name):
        self.name = name
        print("Initialized!")

    def hello(self):
            print("Hello, " + self.name + "!!")

    def goodbye(self):
        print("Good-bye, " + self.name + "!!")

m = Man("Jack Sparrow")
m.hello()
m.goodbye()
