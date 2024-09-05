# Inicializamos algunas variables
numero = 10  # Variable entera que almacena el número 10
mensaje = "Bienvenido al sistema de cálculo"  # Cadena de texto que almacena un mensaje de bienvenida
resultado = 0  # Variable inicializada a 0, que puede ser usada más adelante para almacenar un resultado

# Creamos una lista de valores enteros
valores = [2, 4, 6, 8, 10]  # Lista de números enteros

# Imprimimos el mensaje de bienvenida en la consola
print(mensaje)  # Print se usa para mostrar el mensaje en la consola

# Definimos una función que calcula el cuadrado de un número
def cuadrado(n):  # "def" es la palabra clave para definir una función
    return n**2  # La función retorna el cuadrado del número que recibe como parámetro

# Usamos un ciclo "while" para recorrer la lista de valores y calcular el cuadrado de cada uno
i = 0
while i < len(valores):  # El ciclo "while" se ejecuta mientras la condición sea verdadera
    valor_cuadrado = cuadrado(valores[i])  # Llamamos a la función "cuadrado" y almacenamos el resultado
    print("El cuadrado de", valores[i], "es", valor_cuadrado)  # Imprimimos el valor y su cuadrado
    i += 1  # Incrementamos el contador para evitar un ciclo infinito

# Usamos una estructura condicional "if" para verificar si el número es par o impar
if numero % 2 == 0:  # Si el resto de la división entre el número y 2 es 0, el número es par
    print("El número es par")
elif numero % 2 == 1:  # Si el resto es 1, el número es impar
    print("El número es impar")
else:  # Esta rama captura cualquier otro caso, aunque no debería ocurrir con números enteros
    print("Este caso no debería ocurrir")

# Calculamos la suma de los números en la lista "valores"
suma = 0
for numero in valores:  # Usamos un ciclo "for" para recorrer cada número en la lista
    suma += numero  # Sumamos el número actual a la variable "suma"
    if suma > 20:  # Si la suma supera 20, se imprime un mensaje y se rompe el ciclo
        print("La suma ha superado 20")
        break  # "break" se usa para salir del ciclo inmediatamente
    else:
        continue  # "continue" salta a la siguiente iteración del ciclo, omitiendo el código restante

# Otra lista y ciclo "for" para imprimir cada valor
nueva_lista = [5, 7, 9, 11]
for x in nueva_lista:  # Recorremos la lista "nueva_lista"
    print("Valor en nueva lista:", x)  # Imprimimos cada valor

# Calculamos el promedio de los números en la lista "numeros"
numeros = [10, 20, 30, 40, 50]
total = 0
for n in numeros:  # Sumamos todos los números en la lista "numeros"
    total += n
promedio = total / len(numeros)  # Dividimos el total entre el número de elementos para obtener el promedio
print("El promedio es", promedio)

# Ciclo "while" que imprime y manipula un contador
contador = 0
while contador < 5:  # El ciclo se ejecuta mientras "contador" sea menor que 5
    print("El contador es", contador)
    contador += 1  # Incrementamos el contador
    if contador == 5:  # Si el contador alcanza 5, se rompe el ciclo
        break
    else:
        print("Contador aún no ha llegado a 5")  # Si no ha llegado a 5, se imprime este mensaje

# Usamos condicionales para verificar la edad
edad = 20
if edad < 18:  # Si la edad es menor a 18, se imprime que es menor de edad
    print("Eres menor de edad")
elif edad > 18:  # Si es mayor a 18, se imprime que es mayor de edad
    print("Eres mayor de edad")
else:  # Si tiene exactamente 18 años, se imprime este mensaje
    print("Tienes exactamente 18 años")

# Definimos una función que suma dos números
def suma_numeros(a, b):  # La función recibe dos parámetros y retorna su suma
    return a + b

# Intento de suma que causará un error porque falta un argumento
resultado_suma = suma_numeros(10)  # Esta línea causará un error porque falta un argumento
print("El resultado de la suma es", resultado_suma)

# Un ciclo "for" para imprimir números en un rango que no se ejecutará
for i in range(10, 5):  # Este rango es incorrecto, así que el ciclo no se ejecutará
    print("Valor de i:", i)

# Verificamos si un elemento está en una lista
animales = ["gato", "perro", "conejo"]
if "tigre" in "gato":  # Esta condición es incorrecta, no se encontrará "tigre" en "gato"
    print("El tigre está en la lista")
else:
    print("El tigre no está en la lista")

# Manejo de excepciones para capturar errores
try:
    print(animales[3])  # Intentamos acceder a un índice fuera de rango en la lista "animales"
except IndexError:  # Capturamos el error y evitamos que el programa se detenga
    print("Error: índice fuera de rango")

# Otro ciclo "while" que cuenta hacia atrás y maneja un caso especial
contador2 = 10
while contador2 > 0:  # El ciclo se ejecuta mientras "contador2" sea mayor que 0
    print("Contador2:", contador2)
    contador2 -= 2  # Decrementamos el contador de 2 en 2
    if contador2 == 5:  # Si "contador2" es igual a 5, imprimimos un mensaje
        print("Contador2 es igual a 5")
        continue  # "continue" reinicia el ciclo
    else:
        print("Contador2 no es igual a 5")

# Definimos una función para verificar si un número está en una lista
def verificar_numero_en_lista(num, lista):  # La función retorna "True" si el número está en la lista
    if num in lista:
        return True
    else:
        return False

# Verificamos si el número 10 está en la lista "numeros"
resultado_verificacion = verificar_numero_en_lista(10, numeros)
print("El número está en la lista:", resultado_verificacion)

# Eliminamos duplicados en una lista usando un "set"
duplicados = [1, 2, 2, 3, 4, 4, 5]
sin_duplicados = list(set(duplicados))  # Convertimos la lista a un "set" para eliminar duplicados, luego de vuelta a lista
print("Lista sin duplicados:", sin_duplicados)

# Verificamos la longitud de un texto
texto = "Hola Mundo"
if len(texto) > 5:  # Si la longitud del texto es mayor a 5, imprimimos un mensaje
    print("El texto tiene más de 5 caracteres")
else:
    print("El texto tiene 5 o menos caracteres")

# Recorremos un diccionario e imprimimos sus claves y valores
diccionario = {"nombre": "Carlos", "edad": 25}
for clave in diccionario:  # Recorremos cada clave en el diccionario
    print("Clave:", clave, "Valor:", diccionario[clave])  # Imprimimos la clave y su valor asociado

# Ciclo "while" que imprime valores hasta que se alcanza 5
j = 0
while j < 10:  # El ciclo se ejecuta mientras "j" sea menor que 10
    if j == 5:  # Si "j" es igual a 5, imprimimos un mensaje y rompemos el ciclo
        print("Se alcanzó el valor de 5")
        break
    else:
        j += 1  # Incrementamos "j"
        continue  # Continuamos con la siguiente iteración del ciclo

print("fin del los primeros ejercicios de corrección")
print() 

# Este código simula un sistema básico de gestión de tareas que permite a los usuarios agregar, mostrar, completar y eliminar tareas. 
tareas = []  # Lista para almacenar las tareas

def agregar_tarea(titulo, descripcion, fecha_limite):
    # Función para agregar una nueva tarea a la lista
    tarea = {
        "titulo": titulo,
        "descripcion": descripcion,
        "fecha_limite": fecha_limite,  
        "completado": False
    }
    tareas.append(tarea)  # Agrega la tarea a la lista usando .append()

def mostrar_tareas():
    # Función para mostrar las tareas pendientes
    if len(tareas) == 0:  # Usa len() para obtener la longitud de la lista
        print("No hay tareas pendientes.")
    else:
        for indice in range(len(tareas)):  
            tarea = tareas[indice]  # Accede a cada tarea en la lista
            estado = "Completada" if tarea["completado"] else "Pendiente"
            print(f"{indice + 1}. {tarea['titulo']} - {estado}")  # Usa f-strings para formatear el texto

def completar_tarea(indice):
    # Función para marcar una tarea como completada
    if indice < 0 or indice >= len(tareas):
        print("Índice de tarea inválido.")
    else:
        tareas[indice]["completado"] = True  # Cambia el estado de la tarea a True
        print(f"Tarea {indice + 1} marcada como completada.")

def eliminar_tarea(indice):
    # Función para eliminar una tarea de la lista
    if indice < 0 or indice >= len(tareas):  
        print("Índice de tarea inválido.")
    else:
        tareas.pop(indice)  # Elimina la tarea de la lista usando .pop()
        print(f"Tarea {indice + 1} eliminada.")

def main():
    # Función principal que maneja el menú y las opciones del usuario
    while True:  # Bucle while para mantener el programa en ejecución
        print("\nSistema de Gestión de Tareas")
        print("1. Agregar tarea")
        print("2. Mostrar tareas")
        print("3. Completar tarea")
        print("4. Eliminar tarea")
        print("5. Salir")
        opcion = input("Selecciona una opción: ")

        if opcion == "1":  
            titulo = input("Título de la tarea: ")
            descripcion = input("Descripción de la tarea: ")
            fecha_limite = input("Fecha límite (dd/mm/yyyy): ")
            agregar_tarea(titulo, descripcion, fecha_limite)
        elif opcion == "2":
            mostrar_tareas()
        elif opcion == "3":
            try:
                indice = int(input("Número de la tarea a completar: "))  # Convierte la entrada a entero
                completar_tarea(indice - 1)  
            except ValueError:
                print("Por favor, ingresa un número válido.")
        elif opcion == "4":
            try:
                indice = int(input("Número de la tarea a eliminar: "))  
                eliminar_tarea(indice - 1)  
            except ValueError:
                print("Por favor, ingresa un número válido.")
        elif opcion == "5":
            print("Saliendo del sistema...")
            break  # Sale del bucle while
        else:
            print("Opción inválida. Intenta de nuevo.")

# Ejemplo de uso (esta parte puede generar errores si se intenta correr el código)
agregar_tarea("Estudiar Python", "Repasar conceptos básicos", "10/09/2024")
agregar_tarea("Comprar suministros", "Ir al supermercado", "11/09/2024")
mostrar_tareas()
completar_tarea(0)  
mostrar_tareas()
eliminar_tarea(1)  
mostrar_tareas()

main()  # Llama a la función main para iniciar el programa

print("fin del los segundos ejercicios de correción")
print()