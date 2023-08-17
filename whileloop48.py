# A program that does not stop until you input your name

name = ''
while name != 'Your name':
    print('Enter your correct name:')
    name = input()
    if name == 'Your name':
        print('You are logged in!')
