import datetime

def printTimeStamp(name):
    print("Марчик Денис: " + name)
    print("Час компіляції: " + str(datetime.datetime.now()))
klp = float(input("Давление в килопаскалях: "))
print (0.14503773773 * klp," фунтов на квадратный дюйм\n",7.500637554192 * klp," милиметров ртутного столба\n",0.00986923 * klp," атмосфер")