from modules import *


print("\n")
parking.welcome()
parking.help()
parking.limit(90)
print("\n")

power = False

while power == False:
    x = input("Enter your command: ")

    if x == 'plus':
        try:
            y = int(input("Enter the number of vehicles that are going to park into: "))
        except ValueError:
            print("This is not a number!!! Enter a digit please\n")
        else:
            if y <= 0:
                print("This is wrong")
            else:
                print("\n")
                parking.plus(y)
                parking.commit()

    elif x == 'minus':
        try:
            y = int(input("Enter a number: "))
        except ValueError:
            print("This is not a number!!! Enter a digit please")
        else:
            if y <= 0:
                print("This is wrong")
            else:
                print("\n")
                parking.minus(y)
                parking.commit()

    elif x == 'exit':
        power = True
        parking.exit()

    elif x == 'check':
         y = parking.check()

    elif x == 'help':
        parking.help()

    else:
        print("\n This is not a valid command. Type the right command please." )
        parking.help()