import datetime

def printTimeStamp(name):
    print("Марчик Денис: " + name)
    print("Час компіляції: " + str(datetime.datetime.now()))

a=input("Number of containers below 1 liter : ")
b=input("Number of containers biger 1 liter : ")
print("You get "+"%.2f" % (int(a)*float(0.10)+int(b)*float(0.25))+"$")