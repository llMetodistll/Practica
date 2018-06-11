import datetime
def printTimeStamp(name):
    print('Автор програми: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))

calc = 0
vb = 0
vbp = 0
vbch = 0
vbl = 0


while True:
    vik = int(input("Vvedit svii vik: "))
    if vik == 0:
        break
    calc += 1
    if vik <= 3:
        vbch = "bezkoshtovno"
    elif 3<vik<12:
        vbl = "$" + str(16.00)
    elif vik >= 60:
        vbp = "$" + str(18.00)
    else:
        vb = "$" + str(25.00)


print("Вартість білета: " + (str(vb) + str(vbp) + str(vbl) + str(vbch)))