#Python script to print first N natural numbers.

n = int(input("Please Enter any Number: "))

print("The List of Natural Numbers from 1", "to", n)

for i in range(1, n + 1):
    print(i, end='  ')
