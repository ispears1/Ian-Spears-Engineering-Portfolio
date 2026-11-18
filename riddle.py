def codeBreaker():
    i = 100000
    while i < 1000000:
        four = (str(i))[2:6]
        five = (str(i+1))[1:6]
        middle = (str(i+2))[1:5]
        six = str(i+3)
        if(four == four[::-1]):
            if(five == five[::-1]):
                if(middle == middle[::-1]):
                    if(six == six[::-1]):
                         print(i)
        i = i+1

codeBreaker()