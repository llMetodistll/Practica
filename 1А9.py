import datetime
def printTimeStamp(name):
 print('Автор програми: ' + name)
 print('Час компіляції: ' + str(datetime.datetime.now()))

lr = int(input("Human age: "))
ls = 0
if lr <= 0:
    print("Не волнуйся, если не работает. Если бы все всегда работало, у тебя бы не было работы.")
elif lr == 2 :
    ls = 10.5
elif lr == 1:
    ls = 5.25
else :
    ls = 10.5
    ls += 4 * (lr - 2)
print("Dogs age: " + str(ls))

printTimeStamp("Шульга")