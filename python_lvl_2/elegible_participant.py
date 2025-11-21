while True:
    age = input("Who old are you?: ")
    license = input("Do you have lisence?(y/n): ").strip()
    car = input("Do you have a own or borrowed car?(y/n): ").strip()
    age = int(age)

    if age < 18 or license.lower() == "n" or car.lower() == "n":
        print("You cannot participate")

    elif age >= 18 and license.lower() == "y" and car.lower() == "y":
        print("You can participate")

    else:
        print("You cannot participate")
        
    break