#For loop that iterate from 1 to 100 and print it for the user with an if that replace numbers when they are Fizz, Buzz and FizzBuzz.
for number in range(1, 101):
    if number % 3 == 0 and number % 5 == 0:
        print ("FizzBuzz")
    elif number % 3 == 0:
        print ("Fizz")
    elif number % 5 == 0:
        print ("Buzz")
    else:
        print(number)


