import datetime

def printTimeStamp(name):
    print("Марчик Денис: " + name)
    print("Час компіляції: " + str(datetime.datetime.now()),"\n")
printTimeStamp("Марчик Денис")

x=list(map(str,input()))
myset=set(x)
print(myset)
