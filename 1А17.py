import datetime
def printTimeStamp(name):
    print('Автор програми: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))

summ = int(input("Scolco deneg u tebia "))
god1 = summ + summ * 0.14
print("Za 1 god u tebia %.2f $" % god1)
god2 = god1 + god1 * 0.14
print("Za 2 god u tebia %.2f $" % god2)
god3 = god2 + god2 * 0.14
print("Za 3 god u tebia %.2f $" % god3)


printTimeStamp("Шульга")