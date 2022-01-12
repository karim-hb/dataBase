numbers = input("enter array : (please seprate number with space like 1 2 3 4 ...) :  ")
numbers = numbers.split(" ")
flag = True
for i in range(len(numbers)):
    if numbers[i] == numbers[len(numbers)-1-i]:
        flag = True
    else:
        flag = False    
if flag :
    print("this array is a symmetric")
else:
    print("this array is not a symmetric")