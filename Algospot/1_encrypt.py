number = int(input())
for j in range(number):
    word = str(input())
    n = len(word)
    odd = even = ""
    for i in range(n):
        if i % 2 == 0:
            odd = odd + word[i]
        else:
            even = even + word[i]
    result = odd + even
    print(result)
