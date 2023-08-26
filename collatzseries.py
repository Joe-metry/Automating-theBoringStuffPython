def collatz(number):
    """This is a Collatz function, used to obtain the collatz sequence"""
    if number % 2 == 0:
        even = number // 2
        return even
    else:
        odd = (3 * number) + 1
        return odd


try:
    putNum = int(input('Enter an integer: '))
    while putNum != 1:
        putNum = collatz(putNum)
        print(putNum)
except ValueError:
    print('Only integers must be entered')

