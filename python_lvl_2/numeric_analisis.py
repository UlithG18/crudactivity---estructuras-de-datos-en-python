# P6. Análisis numérico
# Solicita tres números enteros y determina:

# Si los tres son positivos.
# Si al menos uno es negativo.
# Si exactamente uno es cero.
# Debe analizar todas las combinaciones mediante condiciones encadenadas.

numbers = []
value1 = False
value2 = False
value3 = False

while not value1:
    
    number1 = input("Give me a number: ")
    special = "!@#$%^&*()_+-=[]{};:'\",.<>/?\\|"

    if number1.isalpha() : 
        print("You can only enter a number\n")
        continue  

    elif special in number1:
        print("You can only enter a number\n")
        continue

    elif not number1:
        print("\nThe number cannot be empty\n")
        continue 
    
    else:
        number1 = round(float(number1))
        numbers.append(number1)
        value1 = True
        

while not value2:
    
    number2 = input("Give me another me a number: ")
    special = "!@#$%^&*()_+-=[]{};:'\",.<>/?\\|"

    if number2.isalpha() : 
        print("You can only enter a number\n")
        continue  
    
    elif special in number2:
        print("You can only enter a number\n")
        continue

    elif not number2:
        print("\nThe number cannot be empty\n")
        continue 
    
    else:
        number2 = round(float(number2))
        numbers.append(number2)
        value2 = True
       


while not value3:
    
    number3 = input("Give me the last one me a number: ")
    special = "!@#$%^&*()_+-=[]{};:'\",.<>/?\\|"
    
    if number3.isalpha() : 
        print("You can only enter a number\n")
        continue  

    elif special in number3:
        print("You can only enter a number\n")
        continue

    elif not number3:
        print("\nThe number cannot be empty\n")
        continue 
    
    else:
        number3 = round(float(number3))
        numbers.append(number3)
        value3 = True

cont = 0

for z in numbers:
    if z == 0:
        cont += 1

if cont == 1:
    print("There is exact one zero")
    
if number1 > 0 and number2 > 0 and number3 > 0:
    print("All the numbers are positive")

if number1 < 0 or number2 < 0 or number3 < 0:
    print("There is at least one negative number")   

print(numbers)

