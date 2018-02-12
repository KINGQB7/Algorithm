n = int(input())
for i in range(n):
    x = str(input())
    num = int(x.split()[0])
    word = x.split()[1]
    result = word[0:(num-1)] + word[(num):]
    print((i+1) , result)