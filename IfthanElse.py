name = input('Please tell me your name:')
rawage = input('Please tell me your age:')
age = int(rawage)

if age>= 20:
        print('You are allowed in!')
        print('What would you like to drink?')
else:
    print('Too bad',name, "you are not allowed in.")