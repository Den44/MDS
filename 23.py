import datetime

def printTimeStamp(name):
    print("Марчик Денис: " + name)
    print("Час компіляції: " + str(datetime.datetime.now()))

def function(m,n):
    d=int(input("Number:"))
    while int(m)%int(d)and int(n)%int(d):
        d-=1
    print(d)

function(15,10)