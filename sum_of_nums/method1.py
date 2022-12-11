c = 1
ls = []
while c <6:
    n = int(input("Enter a positive number :"))
    if n > 0:
        ls.append(n)
        c += 1
    else:
        print("\"Positive numbers only!\"")
summ = sum(ls)
x = open("method1.txt", "a")
print("Given inputs are : ", ls, file=x)
print("Sum of the inputs = ", summ, file = x)
x.close()