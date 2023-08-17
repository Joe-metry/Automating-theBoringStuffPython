# A program that does not stop until you input your name

name = ''
while name != 'Joseph':
    print('Enter your correct name:')
    name = input()
    if name == 'Joseph':
        print('You are logged in!')
