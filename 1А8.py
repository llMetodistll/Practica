import datetime
def printTimeStamp(name):
    print('Автор програми: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))

nums = int(input("Vvedite 4 znachnyi cod "))
summ1 = nums//1000
summ2 = nums%1000//100
summ3 = nums%1000%100//10
summ4 = nums%1000%100%10
all_summ = summ1 + summ2 + summ3 + summ4

print("You summ is " + str(all_summ))


printTimeStamp("Шульга")