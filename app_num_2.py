def char_split(swears):
    return list(swears)


# Θεωρώ πως το αρχείο κειμένου που δέχεται το πρόγραμμα περιλαμβάνει τις λέξεις κατά γραμμή και όχι την μία δίπλα
# στην άλλη.
file_name = input("Εισάγετε το όνομα του αρχείου χωρίς την κατάληξη .txt: ")
j = 1
line_num = 0
swears = open(file_name + ".txt", "r")
with open(file_name + ".txt", "r") as f:
    for line in f:
        line_num += 1
while j <= line_num:
    char_list = char_split(swears.readline())
    i = 0
    word_length = len(char_list)
    bad_char = 0
    good_char = 0
    while i < word_length:
        if char_list[i] == "f" or char_list[i] == "c" or char_list[i] == "k" or char_list[i] == "r":
            bad_char += 1
        else:
            good_char += 1
        i += 1
    if bad_char > good_char:
        print("Η λέξη είναι κακή.")
    else:
        print("Η λέξη δεν είναι κακή.")
    j += 1
