def main(argv):
    num = int(argv[0])
    old_str = "1"
    for i in range(1,num):
        new_str =  ""
        current_letter = old_str[0]
        current_count = 0
        for letter in old_str:
            if current_letter == letter:
                current_count += 1
            else:
                new_str = new_str + str(current_count) + current_letter
                current_letter = letter
                current_count = 1
        else:
            new_str = new_str + str(current_count) + current_letter
        old_str = new_str
    print(old_str)
