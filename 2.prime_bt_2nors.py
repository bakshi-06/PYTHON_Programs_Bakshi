num1 = int(input("Enter the number 1: "))
num2 = int(input("Enter the number 2: "))
for num in range(num1,num2):
    for i in range(2,num):
        if(num%i==0):
            break
        else:
            print(num)