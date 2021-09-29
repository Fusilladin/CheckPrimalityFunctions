x = int(input('Please choose a number to see if it is prime.  '))

flag = False

if x > 1:
    for elem in range(2, x):
        if (x % elem) == 0:
            flag = True
            break

if flag is True:
    print(print(x, "is not a prime number"))
else:
    print(x, "is a prime number")

# Ask the user for a number and determine whether the number is prime or not. (For those who have forgotten, a prime number is a number that has no divisors.). You can (and should!) use your answer to Exercise 4 to help you. Take this opportunity to practice using functions, described below.
