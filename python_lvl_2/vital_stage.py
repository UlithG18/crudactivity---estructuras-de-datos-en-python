while True:
  
    age = int(input("Who old are you?: "))

    if not age:
        print("The age cannot be empty\n")
        continue

    if not age.isdigit() : 
        print("Enter a valid digit")
        continue   

    if age < 0 or age > 100:
        print("You have to enter a valid number")      
        continue
        
    break
    

while True:
    print("\n--- Occupation ---\n1. Student\n2. Worker\n3. Other/Anything\n")
    occupation = input("What's your occupation?: ").strip()
    
    if not occupation:
        print("You have to enter a number\n")
        continue
    
    if not occupation.isdigit():
        print("You only can enter numbers here\n")
        continue
    
    if occupation < 0 or occupation > 3:
        print("You have to enter a valid number")      
        continue

    break


if age > 60 and (occupation == "1" or "2"):
    print("Not determined case") 

elif age > 60 and occupation != "2":
    print("You're a retired senior")  

elif age > 25 and occupation == "2":
    print("You're an active adult")

elif age >= 18 and age <= 25 and occupation == "1":
    print("You're a university student")

elif age >= 6 and age <= 17 and occupation == "1":
    print("You're a school student")

elif age < 6:
    print("You're an infant")

else:
    print("Not determined case")