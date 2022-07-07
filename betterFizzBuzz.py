def findDivisible(num, divisible):
    return num % divisible == 0


def fizzBuzz(input):
    if(findDivisible(input, 3)) and (findDivisible(input, 5)):
        return "FizzBuzz"
    if(findDivisible(input, 3)):
        return "Fizz"
    if(findDivisible(input, 5)):
        return "Buzz"
    else:
        return input


for i in range(100):
    print(fizzBuzz(i))
