# Solicita edad y respuesta a la pregunta: “¿Te gusta programar?” (sí/no). 
# El programa debe repetirse mientras la edad ingresada sea mayor a cero. 
# Al finalizar, muestra cuántas respuestas fueron afirmativas y cuántas negativas. 
# Controla respuestas vacías o incorrectas dentro del ciclo.

answer = 1
cont1 = 0
cont2 = 0

while answer > 0:
    
    like = input("\nDo you like programming?(y/n): ").strip().lower()
    
    if not like:
        print("\nThe response cannot be empty\n")
        continue 

    if like == "y":
        cont1 += 1
    
    elif like == "n":
        cont2 += 1

    else:
        print("Try againg with a correct answer\n")
        continue
        
    answer = input("Which is your age?: ")
    special = "!@#$%^&*()_+-=[]{};:'\",.<>/?\\|"

    if answer.isalpha() : 
        print("\nYou can only enter a number\n")
        continue  

    elif special in answer:
        print("\nYou can only enter a number\n")
        continue

    elif not answer:
        print("\nThe number cannot be empty\n")
        continue 

    else:
        answer = int(answer)

print(f"The positive answers was {cont1} | The negative answers was {cont2}")

    
    



