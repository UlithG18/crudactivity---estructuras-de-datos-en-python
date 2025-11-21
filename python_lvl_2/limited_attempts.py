import time
print("\n--- Riwi's computer log in ---\n")
print("--- Antony's group ---\n")

# user = Turing
# password = Qwe.123*
cont = 0

while cont != 3:
    data1 = input("Enter your user: ").lower().strip()

    if not data1:
        print("\nThe user cannot be empty\n")
        continue

    if not data1.isalpha() : 
        print("The user only contains alphabetic characters\n")
        cont += 1
        continue   

    if not len(data1) == 6:
        print("The user contains six characters\n")      
        cont += 1
        continue
    
    if data1 == "turing":
        print("You got it\n")
        user = data1

while cont != 3:
    
    data2 = input("Enter your password: ").strip().lower()
    special = "!@#$%^&*()_+-=[]{};:'\",.<>/?\\|1234567890qazxswedcvfrtgbnhyujmkiolñp"

    if not data2:
        print("\nThe password cannot be empty\n")
        continue

    if not len(data2) == 8:
        print("The password contains eighth characters\n")
        cont += 1      
        continue

    if not special in data2: 
        print("The password contains letters, numbers and special characters\n")
        cont += 1
        continue   
    
    if data2 == "qwe.123*":
        print("You have access\n")
        password = data2
        
print("Many attempts, try it again\n")