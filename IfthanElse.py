name = input('Please tell me your name:')
rawage = input('Please tell me your age:')
age = int(rawage)

if age>= 20:
        print('You are allowed in!')
        print('What would you like to drink?')
elif age >= 18:
    print('You are allowed in')
    print("But you are not allowed to drink, please feel free to advance")
else:
    print('Too bad',name, "you are not allowed in.")