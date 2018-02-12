n = int(input())
for i in range(n):
    input_1 = str(input())
    input_2 = str(input())
    input_3 = str(input())

    input_x = [input_1.split()[0], input_2.split()[0], input_3.split()[0]]
    input_y = [input_1.split()[1], input_2.split()[1], input_3.split()[1]]

    s_x = list(set(input_x))
    s_y = list(set(input_y))

    if (input_x.count(s_x[0]) == 1):
        out_x = s_x[0]
    else:
        out_x = s_x[1]
    if (input_y.count(s_y[0]) == 1):
        out_y = s_y[0]
    else:
        out_y = s_y[1]

    print(out_x, out_y)
