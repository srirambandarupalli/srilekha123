    string = input("")
    counter = 0
    for x in string:
        if x == ' ' or x == '\n':
            counter += 1
    print(counter)
