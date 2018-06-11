import datetime
def printTimeStamp(name):
    print('Автор програми: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))

lst = [1, 2, 3, 4, 5,]

print(lst)

printTimeStamp("Шульга")