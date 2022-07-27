import random
pencils_str = input('How many pencils would you like to use:')
while pencils_str.isnumeric() == False or pencils_str == '0':
    if pencils_str.isnumeric() == False:
        pencils_str = input('The number of pencils should be numeric')
    if pencils_str == '0':
        pencils_str = input('The number of pencils should be positive')
pencils = int(pencils_str)
name = input("Who will be the first (John, Jack):")
while name != "Jack" and name != "John":
    name = input("Choose between 'John' and 'Jack'")

print('|' * pencils)
while pencils > 0:
    print(name + "'s turn:")
    if name == 'John':
        x_str = input()
        while (x_str != '1' and x_str != '2' and x_str != '3') or int(x_str) > pencils:
            if x_str != '1' and x_str != '2' and x_str != '3':
                x_str = input("Possible values: '1', '2' or '3'")
            if x_str.isnumeric() == True:
                if int(x_str) > pencils:
                    x_str = input("Too many pencils were taken")
        x = int(x_str)
    else:
        if pencils % 4 == 1 and pencils != 1:
            x = random.randrange(1, 3, 1)
        elif pencils % 4 == 2:
            x = 1
        elif pencils % 4 == 3:
            x = 2
        elif pencils % 4 == 0:
            x = 3
        elif pencils <= 2:
            x = 1
        print(x)
    pencils -= x
    print('|' * pencils)
    if name == "John":
        name = "Jack"
    else:
        name = "John"
    if pencils == 0:
        print(name + " won!")
