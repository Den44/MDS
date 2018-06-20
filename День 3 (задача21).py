import datetime
def printTimeStamp(name):
    print('Марчик Денис: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))

t = open("samp.txt", 'a')
t.write("\n\nPifagor F.P.")

t.close()


