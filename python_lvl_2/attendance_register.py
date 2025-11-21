name_list = []
repeat_list = []

cont1 = 0
cont2 = 0

print("Enter 'End' to finish")

while True:
    # print(name_list,repeat_list)

    name = input("Enter a name: ").strip()  

    if not name.isalpha():
        print("Invalid name")
        continue
    
    if name.lower() == "end":
        break

    if name == "":
        continue
    
    if name in name_list:
        if name not in repeat_list:
            repeat_list.append(name)
            cont2 += 1
    
    name_list.append(name)
    cont1 += 1

print(f"Total of names: {cont1}")
print(f"Total of repeat names: {cont2}")