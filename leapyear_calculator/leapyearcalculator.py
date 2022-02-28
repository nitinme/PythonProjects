print("Welcome to the Leap year Calculator!") # Introduction
print("Lets Get Started!")
print('--------------------------------------------------')
year = int(input("Enter The Year that You Want To Check: ")) # Inputting what year the user wants to check


# percent sign stands for modulus, which means get the remainder, so when we do year % 4 we are doing year/4 and getting the remainder of the equation

if year % 4 == 0: #using if loop on remainder of 0 to see if remainder is 0. if remainder is 0, then year is perfectly divisible by 4, making it a leap year. else, it is not a leap year.
    if year % 100 ==  0:
        print("The year {0} is not a leap year.".format(year))
    else:
        print("The year {0} is a leap year.".format(year))
else:
    print("The year {0} is not a leap year.".format(year))