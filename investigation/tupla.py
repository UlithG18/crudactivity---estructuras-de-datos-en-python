# P3. Tuplas — Catálogo estático
# Crear una tupla con seis valores numéricos distintos. Debido a que no se puede modificar directamente, 
# se debe mostrar el resultado de cada operación sin alterar la tupla original:

# Cómo quedaría si se agregara un nuevo valor al final.
# Cómo quedaría si un valor se reemplazara por otro.
# Cómo quedaría si se eliminara un valor por su posición.
# Mostrar todos los valores con sus posiciones.
# Además, se debe determinar manualmente:

# El valor mayor.
# El valor menor.
# La suma total.
# La posición del mayor.


values = (102,23,75,46,97,23)

print("\nOriginal tuple:")
print(values)

# Add a value at the end 

new_value = 99
added = values + (new_value,)
print("\nIf a new value is added at the end:")
print(added)

# Replace a value 

pos_replace = 2
new_number = 100

if pos_replace >= 0 and pos_replace < len(values):
    replaced = values[:pos_replace] + (new_number,) + values[pos_replace+1:]
    print("\nIf the value at position", pos_replace, "is replaced:")
    print(replaced)
else:
    print("\nInvalid position for replacement")

# Remove a value by position 

pos_remove = 3

if pos_remove >= 0 and pos_remove < len(values):
    removed = values[:pos_remove] + values[pos_remove+1:]
    print("\nIf the value at position", pos_remove, "is removed:")
    print(removed)
else:
    print("\nInvalid position for removal")

# Show values with positions

print("\nValues with positions:")
i = 0
for v in values:
    print(i, "->", v)
    i += 1

# Manual calculations

largest = values[0]
largest_pos = 0

i = 1
for n in values[1:]:
    if n > largest:
        largest = n
        largest_pos = i
    i += 1

smallest = values[0]
for n in values[1:]:
    if n < smallest:
        smallest = n

total = 0
for n in values:
    total += n

print("\nLargest value:", largest)
print("Position of largest:", largest_pos)
print("Smallest value:", smallest)
print("Total sum:", total)




