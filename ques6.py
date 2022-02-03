#Python script to calculate sum of first N natural numbers.

N = int(input("Enter a natural number: "))
num=0
for i in range(0,N+1):
    num= num + i;
print(num)