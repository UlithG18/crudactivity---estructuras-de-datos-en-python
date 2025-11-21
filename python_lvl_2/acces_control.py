black_list = ("ulith", "samuel", "valentina")
user = input("\nWhich is your user: ").lower()

if user in black_list:
    print("\nYou don't have access, you'r in the black list\n")

else:  
    print("Correct user\n")
    code = int(input("Which is your code: "))

    if code % 2 == 0 or code % 10 == 7:
        print("\nYou have access")

    else:
        ("\nYou don't have access, invalid code")
        
