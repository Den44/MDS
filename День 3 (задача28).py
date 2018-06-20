import datetime
def printTimeStamp(name):
    print('Марчик Денис: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))




t = open('samp.txt', 'r')
for i in range(10):
    print(t.readline())

t.close()


