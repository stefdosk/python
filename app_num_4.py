def app_4(string):
    def char_split(string):
        return list(string)

    x = char_split(string)
    b = len(x)
    i = 0
    asc = [None] * b

    while i < b:
        asc[i] = str(ord(x[i]))
        i += 1

    joined_asc = int("".join(asc))

    for i in range(2, joined_asc // 2):
        if (joined_asc % i) == 0:
            print(
                "Ο αριθμός που προκύπτει από την μετατροπή του αρχικού string σε αναπαράσταση ASCII δεν είναι πρώτος και είναι ο: " + str(
                    joined_asc))
            break
    else:
        print(
            "Ο αριθμός που προκύπτει από την μετατροπή του αρχικού string σε αναπαράσταση ASCII είναι πρώτος και είναι ο: " + str(
                joined_asc))


# Κλήση συνάρτησης για έλεγχο λειτουργικότητας
app_4(input("Εισάγετε ένα string: "))
