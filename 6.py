def print_trianggle(n, k) :
    res = 1
    if (k > n - k) :
        k = n - k
    for i in range(0 , k) :
        res = res * (n - i)
        res = res // (i + 1)
    
    return res

def printPascal(n) :
    for line in range(0, n) :

        for i in range(0, line + 1) :
            print(print_trianggle(line, i),
                " ", end = "")
        print()
    


n = input("please enter the rows : ")
printPascal(int(n))
