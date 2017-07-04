# collatz function practice project

def collatz(number):
    if (number % 2 == 0):
        # even number
        print ('number // 2')
        return number // 2
    elif (number % 2 == 1):
        # odd number
        print ('3 * ' + str(number) + ' + 1')
        return 3 * number + 1

print ('Provide an integer to test')
numtest = int(input())

collatz(numtest)


