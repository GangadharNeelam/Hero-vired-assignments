car = {}
n = int(input("Enter number of key-value pairs :"))
for i in range(n):
    key = input("Enter car brand :")
    value = input("Enter colour of the car :")
    car.update({key:value})
x = open("dict_01.txt", "a")
print("Output dictionary :", "\n", car, file=x)
x.close()