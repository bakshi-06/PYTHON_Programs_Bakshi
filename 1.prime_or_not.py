print("Enter the Number: ")
num = int(input())
for i in range(2,num):
    if num % i == 0:
        break
    else:
        print('it is prime no')