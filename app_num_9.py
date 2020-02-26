pos_int = False
while not pos_int:
    try:
        num = int(input("Εισάγετε έναν ακέραιο θετικό αριθμό: "))
        if num > 0:
            pos_int = True
        else:
            print("Ο αριθμός που εισάγατε δεν ήταν θετικός ακέραιος.")
    except ValueError:
        print("Ο αριθμός που εισάγατε δεν ήταν θετικός ακέραιος.")
res = (num * 3) + 1
dig_num = int(len(str(res)))
i = 0
sum1 = 0
sum2 = 0
while i <= dig_num:
    sum1 += res % 10
    res = res // 10
    i += 1
if sum1 // 10 != 0:
    sum1 = (sum1 * 3) + 1
    for i in range(0, 2):
        sum2 += sum1 % 10
        sum1 = sum1 // 10
    print("Ο μονοψήφιος αριθμός στον οποίο καταλήξαμε είναι ο: " + str(sum2))
else:
    print("Ο μονοψήφιος αριθμός στον οποίο καταλήξαμε είναι ο: " + str(sum1))
