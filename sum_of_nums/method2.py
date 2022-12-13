# To add sum of positive numbers
n = int(input("Number of inputs : "))
ls = []
for i in range(n):
    while True:
        m = int(input("Enter a number :"))
        if m >= 0:
            ls.append(m)
            break
        else:
            print("Postive numbers only!")
summ = sum(ls)
x = open("method2.txt", "a")
print("Given inputs are : ", ls, file=x)
print("Sum of the inputs = ", summ, file = x)
x.close()
