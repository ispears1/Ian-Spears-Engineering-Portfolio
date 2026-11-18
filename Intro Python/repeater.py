def repeater(word, num1, num2):
    word = word[:num1]
    for i in range(num2):
        print(word, end='')

ur_word = input()
length = int(input())
times = int(input())

repeater(ur_word, length, times)
