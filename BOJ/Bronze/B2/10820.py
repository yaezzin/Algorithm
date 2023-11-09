while True:
    try:
        str= input()
        
        lower_count = 0
        upper_count = 0
        number_count = 0
        bin_count = 0

        for s in str:
            if s.islower():
                lower_count += 1
            if s.isupper():
                upper_count += 1
            if s.isnumeric():
                number_count += 1
            if s == ' ':
                bin_count += 1

        print(lower_count, upper_count, number_count, bin_count)

    except:
        break