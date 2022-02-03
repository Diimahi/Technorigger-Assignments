#Python script to check prime number.

n=int(input("Enter the number"))
a=1
for i in range(2,n):
    if n%i==0:
        a=0
        if a==1:
            print("number is prime")
        else:
            print("number is not prime")
