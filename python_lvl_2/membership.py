value = False

while not value:
    print("\n--- Types of Amount ---\n0 - 20000 = Low\n21000 - 50000 = Average\n51000 - 100000 = High\n")
    price = input("How much did you spend?: ")
    special = "!@#$%^&*()_+-=[]{};:'\",.<>/?\\|"

    if price.isalpha() : 
        print("You can only enter a number\n")
        continue  

    if special in price:
        print("You can only enter a number\n")
        continue

    if not price:
        print("\nThe number cannot be empty\n")
        continue
    
    value = float(price)

classification = False

while not classification:

    print("\n--- Types of Membership ---\n1.Active\n2.Temporal\n3.Any\n")
    membership = input("Which memebership you have?: ").strip()

    if value >= 51000 and membership == "1":
        print("Your classification is Premium")
        classification = True

    elif 50000 >= value >= 21000   or membership == "2":
        print("Your classification is frequent")
        classification = True

    else:
        print("Your classification is Regular")
        classification = True
    