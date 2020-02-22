num1 = float(input("Εισάγετε έναν αριθμό: "))
num = abs(int(num1))
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
    for i in range(0, 2):
        sum2 += sum1 % 10
        sum1 = sum1 // 10
    print("Ο μονοψήφιος αριθμός στον οποίο καταλήξαμε είναι ο: " + str(sum2))
else:
    print("Ο μονοψήφιος αριθμός στον οποίο καταλήξαμε είναι ο: " + str(sum1))
