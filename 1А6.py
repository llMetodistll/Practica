import datetime
def printTimeStamp(name):
    print('Автор програми: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))


money = float(input("Сколько ти должен "))
all_money = (money + money*0.14) + (money * 0.18)
print("Ти заплатиш %.2f $" % all_money)

printTimeStamp("Шульга")