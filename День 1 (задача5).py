import datetime

def printTimeStamp(name):
    print("Марчик Денис: " + name)
    print("Час компіляції: " + str(datetime.datetime.now()))
name=str(input("Print your name: "))
print("Hello,"+name)