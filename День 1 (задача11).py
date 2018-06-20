def printTimeStamp(name):
    print("Марчик Денис: " + name)
    print("Час компіляції: " + str(datetime.datetime.now()))
sm = float(input("Введите свой рост в сантиметрах: "))
print("Дюймы: ",sm / 2.54 , "\nФуты: ", sm / 30.48)

