# Python script to print first 10 even naturals numbers.

maximum = int(input(" Please Enter the Maximum Value : "))

for number in range(1, maximum+1):
    if(number % 2 == 0):
        print("{0}".format(number),end=' ')