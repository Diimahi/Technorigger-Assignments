#Python program to check divisibility of a number by 5

number = int(input(" Please Enter any Positive Integer : "))
if(number % 5 == 0):
    print("Given Number {0} is Divisible by 5".format(number))
else:
    print("Given Number {0} is Not Divisible by 5".format(number))
