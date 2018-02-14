import parser
n_iter = int(input())
for i in range(n_iter):
    str_input = str(input())
    str_split = str_input.split()
    A = str_split[0]
    operator = str_split[1]
    if operator not in ["+", "*", "-"]:
        print("No")
        continue
    B = str_split[2]
    C = str_split[4]
    str_number = dict(zero=0, one=1, two=2, three=3, four=4, five=5, six=6, seven=7, eight=8, nine=9, ten=10)
    a = str(str_number.get(A))
    b = str(str_number.get(B))
    formula_c = a + operator + b
    code = parser.expr(formula_c).compile()
    c = eval(code)
    if (c < 0) or (c > 10):
        print("No")
        continue
    else:
        str_c = list(str_number.keys())[c]
        if (len(str_c) != len(C)) or (set(str_c) != set(C)):
            print("No")
            continue
        else:
            temp = list(set(C))
            for ss in range(len(set(C))):
                if (str_c.count(list(set(C))[ss])) == (C.count(list(set(C))[ss])):
                    temp[ss] = 1
                else:
                    temp[ss] = 0
            if len(set(C)) == sum(temp):
                print("Yes")
            else:
                print("No")
