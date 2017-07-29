# 1.3 Pythonインタプリタ
# 1.3.1 算術計算
print("# 1.3.1")
print(1 + 2)
print(4 * 5)
print(7 / 5)
print(3 ** 2)

# 1.3.2 データ型
print("# 1.3.2")
print(type(10))
print(type(2.718))
print(type("hello"))

# 1.3.3 変数
print("# 1.3.3")
x = 10
print(x)
x = 100
print(x)
y = 3.14
print(x * y)
print(type(x * y))

# 1.3.4 リスト
print("# 1.3.4")
a = [1, 2, 3, 4, 5]
print(a)
print(len(a))
print(a[0])
print(a[4])
a[4] = 99
print(a)
print(a[0:2])
print(a[1:])
print(a[:3])
print(a[:-1])
print(a[:-2])

# 1.3.5 ディクショナリ
print("# 1.3.5")
me = {"height": 177}
print(me["height"])
me["weight"] = 60
print(me)

# 1.3.6 ブーリアン
print("# 1.3.6")
hungry = True
sleepy = False
print(type(hungry))
print(not hungry)
print(hungry and sleepy)
print(hungry or sleepy)

# 1.3.7 if文
print("# 1.3.7")
hungry = True
if hungry:
    print("I'm hungry.")
hungry = False
if hungry:
    print("I'm hungry.")
else:
    print("I'm not hungry.")
    print("I'm sleepy.")

# 1.3.8 for文
print("# 1.3.8")
for cnt in [1, 2, 3]:
    print(cnt)

# 1.3.9 関数
print("# 1.3.9")
def hello():
    print("Hello, Python World!!")
hello()

def hello(object):
    print("Hello, " + object + "!!")
hello("cat")