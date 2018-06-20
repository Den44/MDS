import datetime

def printTimeStamp(name):
    print("Марчик Денис: " + name)
    print("Час компіляції: " + str(datetime.datetime.now()))
s = list(map(int,input("Введите количество штучек и штукенций через пробел: ").split()))
print("Общая масса: ",(75 * s[0]) + (112 * s[1]),"грамм")

