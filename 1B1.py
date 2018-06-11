import datetime
def printTimeStamp(name):
    print('Автор програми: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))

P = int(input("Тиск газу: "))
V = int(input("Об'єм газу: "))
R = 8.314
T = int(input("Температура: "))
Kel = T + 273.15

n = (P * V) / (R * T)

print("Молярна маса газу = " + str(n))

printTimeStamp("Шульга")