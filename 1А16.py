import datetime
def printTimeStamp(name):
 print('Автор програми: ' + name)
 print('Час компіляції: ' + str(datetime.datetime.now()))

d = int(input("Довжина поля: "))
sh = int(input("Ширина поля: "))
Sa = d * sh / 100
Sg = d * sh / 10000

print("Площа поля в: \n" + str(Sa) + " Арах\n" + str(Sg) + " Гектарах")

printTimeStamp("Шульга")