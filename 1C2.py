import datetime
def printTimeStamp(name):
    print('Автор програми: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))

god = int(input("Рік: "))
ms = int(input("Місяць: "))
den = int(input("День: "))

