# Listas

Las listas en Python son secuencias ordenadas y mutables de elementos que pueden contener datos de diferentes tipos. Proporcionan una manera eficiente de almacenar y manipular datos, permitiendo realizar operaciones como acceder a elementos por índice, agregar, eliminar o modificar elementos.


# Principales características de las listas en Python

- Mutabilidad
- Acceso por indice
- Diversidad de tipos

# Métodos para las listas

Las listas tienen métodos propios para facilitarte el manejo de ellas mismas.


# Métodos de listas y su resultado

x.append(e) → Agrega a la lista x el elemento e

x.insert(i, e) → Inserta e en la posición i de la lista x

x.count(e) → Conteo de instancias de e en la lista x

x.remove(e) → Elimina el primer elemento e de la lista x

x.pop(i) → Entrega el elemento en la posición i en la lista y lo elimina

x.index(e) → Entrega la posición del primer elemento e en x

x.sort() → Ordena x en forma creciente

x.reverse() → Invierte la lista x

x.clear() → Vaciar la lista x

x.copy() → Entrega una copia por referencia de una lista de un nivel


# ¿Por qué las listas son mutables?

Las listas en Python son mutables porque su estructura interna permite modificar directamente los elementos almacenados en ellas, es decir, la lista conserva una referencia a un bloque de memoria que puede cambiarse sin necesidad de crear un nuevo objeto, lo que facilita que podamos agregar, eliminar o reemplazar elementos en cualquier momento sin reconstruir toda la colección.

# Situaciones donde resultan útiles

Las listas son especialmente prácticas cuando necesitamos colecciones de datos que cambien constantemente, por ejemplo, inventarios de un juego que se actualizan a medida que el jugador recoge objetos, listas de tareas donde agregamos o quitamos actividades según sea necesario, o cualquier situación donde los datos no permanezcan estáticos y el programa tenga que modificarlos continuamente.

# Ejemplo básico de creación, lectura, modificación y eliminación


mi_lista = [10, 20, 30]     # creación de la lista
print(mi_lista[1])          # lectura del elemento en la posición 1
mi_lista[1] = 99            # modificación del valor en esa posición
mi_lista.pop()              # eliminación del último elemento



# Tuplas

Las tuplas son secuencias ordenadas e inmutables de elementos, lo que significa que una vez creadas, sus elementos no pueden ser modificados. A pesar de esta limitación, las tuplas son útiles cuando se requiere mantener un conjunto de datos estático o cuando se desea evitar cambios accidentales en la estructura de los datos. 

# Principales características de las tuplas en Python

- Características clave de los diccionarios
Inmutabilidad
- Acceso por indice
- Diversidad de tipos
- Datos duplicados
- Resumen

# Por qué son inmutables

Las tuplas son inmutables porque Python las almacena como secuencias fijas cuyo contenido no puede ser alterado una vez creado, lo cual garantiza que los datos permanezcan constantes y evita modificaciones accidentales, además de permitir que la tupla pueda ser usada como clave en un diccionario o como parte de estructuras que requieren seguridad e integridad de información.

# Situaciones donde resultan útiles

Las tuplas son muy útiles cuando necesitamos representar datos que no deben cambiar durante la ejecución del programa, por ejemplo, coordenadas de un punto en un mapa, valores de configuración que deben permanecer intactos, o conjuntos de datos que describen características estáticas como el tamaño de una imagen, todo esto ayuda a evitar errores por cambios inesperados.

# Ejemplo 

tupla = (5, 10, 15)
print(tupla[0])      
for elemento in tupla:
    print(elemento)  


# Diferencias clave frente a listas y tuplas

A diferencia de las listas y tuplas, que se acceden mediante índices numéricos, los diccionarios permiten acceder a la información a través de claves únicas que describen el valor asociado, lo que hace más intuitivo su uso cuando los datos representan atributos de un objeto, además, los diccionarios pueden modificarse libremente igual que las listas, pero mantienen la estructura de pares clave-valor que los hace especialmente flexibles y expresivos.

# Ejemplo 


persona = {"nombre": "Ana", "edad": 20}

persona["ciudad"] = "Bogotá"     # agregar un nuevo par clave-valor
print(persona["nombre"])         # consultar un valor existente
persona["edad"] = 21             # modificar un valor ya guardado
del persona["ciudad"]            # eliminar un valor




# Diccionarios

Continuando con la lección de colecciones, ahora nos centraremos en los diccionarios ya que ellos son colecciones no ordenadas de pares clave-valor. A diferencia de las listas y tuplas, que se acceden por índice numérico, los diccionarios utilizan claves únicas para acceder a sus valores.

Dict = {

"clave": valor,

"clave": valor,

"clave": valor...

}

Es fundamental que los domines porque su estructura es muy similar al manejo de objetos en otros lenguajes de programación, por ejemplo, imagina que quieres guardar tu información personal en Python, tu nombre, edad, dirección, etc. Puedes usar un diccionario para esto.

# Características clave de los diccionarios

# Claves Únicas:

Cada clave en un diccionario debe ser única. Si intentas usar la misma clave más de una vez, el valor más reciente sobrescribirá al anterior.

# Claves Inmutables

Las claves deben ser de un tipo de datos inmutable, como cadenas, números o tuplas (con elementos inmutables). Esto se debe a que las claves deben ser únicas y no pueden cambiarse una vez establecidas.

# Valores Mutables

Los valores en un diccionario pueden ser de cualquier tipo de datos, incluyendo listas, otros diccionarios, etc. 

# Métodos útiles

Cada uno de esos métodos puede utilizar un ciclo for para iterar sobre ellos. dándote una facilidad en el manejo de los diccionarios.

# keys()

Devuelve todas las claves del diccionario en un dict_keys, para facilitar su posterior manejo te recomiendo convertirlo en una lista

# Item()

Devuelve una dict_items ,esta colección contiene una lista con tuplas que contienen el par clave-valor, como ya sabes la tupla no puede ser modificada 

# Values()

Devuelve todos los valores del diccionario en un dict_values

get(clave, valor_por_defecto)

Retorna el valor asociado a la clave si existe, de lo contrario retorna valor_por_defecto, es muy útil ya que cuando intentamos acceder a una clave que no existe nos arroja una excepción, en cambio con este método controlamos dicha excepción.

# Match-Case

El patrón match-case es una estructura que permite realizar comparaciones múltiples de una manera más clara y organizada, ya que funciona como un sistema de coincidencia de patrones donde el programa evalúa un valor y ejecuta el bloque de código correspondiente al primer caso que coincida, lo cual hace que el código sea más legible cuando se manejan condiciones especificas.

# ¿Para qué se usa?

Se utiliza para simplificar decisiones donde existen múltiples caminos posibles según el valor proporcionado por el usuario o el estado de una variable, permitiendo escribir código más declarativo y fácil de entender, especialmente cuando las alternativas son muchas o cuando se requieren patrones más específicos que un simple if o elif.

# Diferencias frente a if y elif

A diferencia de if y elif, que evalúan condiciones lógicas una por una, match-case realiza una coincidencia directa con patrones, lo que evita repetir comparaciones largas y hace que el código sea más ordenado, además, ofrece capacidades avanzadas como patrones estructurados y extracción de valores, cosas que las condiciones tradicionales no manejan de forma tan limpia.

# Situaciones donde usarlo puede ser más claro

Resulta más claro cuando el programa debe responder a muchas opciones posibles, como menús con múltiples alternativas, clasificación de datos según su tipo o estructura, o sistemas donde las decisiones dependen directamente del valor recibido y no tanto de expresiones lógicas complejas.

# Ejemplo sencillo

opcion = input("Ingresa una opción: ")

match opcion:
    case "1":
        print("Elegiste la opción uno")
    case "2":
        print("Elegiste la opción dos")
    case _:
        print("Opción no válida")
