import datetime

def printTimeStamp(name):
    print("Марчик Денис: " + name)
    print("Час компіляції: " + str(datetime.datetime.now()))
for i in range(1,11):
    print(" ")
    for z in range(1,11):
        print(i*z, end="\t")