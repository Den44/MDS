import datetime


def printTimeStamp(name):
    print("Марчик Денис: " + name)
    print("Час компіляції: " + str(datetime.datetime.now()))

a=list(map(int, input("Numbers:").split()))
list1=[]
List=[i for i in range(1,15)]
c=4/(a[0]*a[1]*a[2])
count=0
nak=0
for i in range (15):
    c = 4 / ((a[0]+count )* (a[1]+count) * (a[2]+count))
    count+=2
    list1.append(c)
for i in list1:
    for j in (List):
        if j%3==0:
            nak= +
        else:
            nak="-"
print(nak.join(str(x) for x in list1))