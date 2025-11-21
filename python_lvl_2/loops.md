# Investigación sobre bucles


Los bucles permiten que un programa repita acciones varias veces, ya sea controlando cuántas veces ocurre la repetición o verificando una condición que puede cambiar con el tiempo, son fundamentales para automatizar tareas y evitar escribir código repetitivo.


# 1. Diferencias entre un bucle controlado por contador y uno controlado por condición


# Bucle controlado por contador


Es un bucle donde sabemos desde el inicio cuántas veces se repetirá la acción, normalmente se implementa con un for, usando un rango o una colección.

La repetición está ligada a un contador que avanza automáticamente, usado norlmalmente cuando el número de iteraciones se conoce.

Ej:

for i in range(5):  
    print("Hola")

Se repite 5 veces


# Bucle controlado por condición

En este tipo de bucle, la repetición depende de si una condición es verdadera o falsa, se implementa con while y continúa hasta que la condición cambie, la cantidad de veces que se repite dependerá de la condición, la condición puede depender de variables que cambian dentro del ciclo.

Ej:

contador = 0
while contador < 5:
    print("Hola")
    contador += 1


# 2. Ejemplos cotidianos


# Ejemplo de bucle controlado por contador


- Hacer 10 sentadillas, ya sabes cuántas repeticiones debes hacer


# Ejemplo de bucle controlado por condición


- Esperar a que el semáforo se ponga en verde, no sabes cuánto se demorará en cambiar


# 3. Cuándo es más apropiado usar while en lugar de for

Es mejor usar el while cuando:

- No sabes cuántas veces se repetirá la acción

- La repetición depende de una condición que puede cambiar durante el proceso

- La lógica del ciclo se basa en esperar un evento, no en contar elementos

Ej:

- Leer datos hasta que el usuario escriba "salir"

- Repetir un menú o pregunta hasta que la opción o respuesta dada sea válida


# 4. Qué es un bucle infinito, cómo prevenirlo y cómo detectarlo


Un bucle infinito es un ciclo que nunca termina, porque la condición siempre sigue siendo verdadera, para prevenirlo es necesario asegurarse de que algo dentro del bucle modifique la condición, usando contadores o flags.

Ej:

while True:
    print("Esto nunca se detiene")

# Dectención durante la ejecución

- El programa no avanza a la siguiente instrucción

- La terminal imprime sin parar

- El CPU empieza a subir su uso

- El programa no responde o no regresa al menú

# 5. Función de break y continue dentro de un ciclo

# break

- Detiene el ciclo por completo, aunque la condición siga siendo verdadera

- Se usa cuando hay una razón para salir inmediatamente

Ej:

while True:
    respuesta = input("Cuál es tu edad?: ")
    if respuesta == "0":
        break  

# continue

- Salta la iteración actual y pasa a la siguiente

- Para omitir casos específicos sin detener todo el bucle

Ej:

for num in range(5):
    if num == 2:
        continue  # Se salta el 2
    print(num)

# 6. Error lógico más común al usar while y cómo evitarlo

Olvidar actualizar la condición dentro del while, provocando un bucle infinito

Ej:

contador = 0
while contador < 5:
    print(contador)
    
Para evitarlo es necesario:

- Revisar que la condición cambie dentro del ciclo.

- Preguntarse, ¿Qué hará que este while deje de cumplirse?

- Usar prints para ver si las variables avanzan

- Establecer banderas