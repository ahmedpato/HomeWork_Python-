# By : Ahmed Mohammed Ali / 20184020
Number = int(input("Enter Your Number :"))
factorial = 1
if Number < 0 :
    print ("Error, please enter a number greater than 0, to find the factorial of the number")
elif Number == 0 :
    print("The Factorial of 0 is 0")
else:
    for i in range(1,Number+1):
        factorial = factorial*i
    print("The Factorial of",Number,":",factorial)
