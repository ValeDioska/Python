# Dada una lista de palabras, cuenta cuántas veces aparece la palabra "Python" en la lista.
lista = ["Python", "Java", "C++", "Python", "JavaScript", "Python", "C#"]

print(lista)
print("El numero de veces que aparce Python es de", lista.count("Python"))

print()

# Dada una lista de cadenas de texto, convierte todas las cadenas a mayúsculas sin usar métodos como upper().
frases = ["hola", "mundo", "python", "es", "genial"]

print(frases)
print("frase a mayuscula")
for i in range(len(frases)):
    frases[i] = "".join([chr(ord(c) - 32) for c in frases[i]])
print(frases)

print()

# Dada una lista de palabras, elimina todas aquellas palabras que tengan menos de 4 caracteres.
palabras = ["sol", "luna", "cielo", "mar", "estrella", "pez"]

print(palabras)
print("palabras que tengan más de 4 caracteres")
palabras = [palabra for palabra in palabras if len(palabra) >= 4]
print(palabras)

print()

# Dada una lista de números, encuentra el número máximo sin usar la función max().
num = [15, 22, 8, 34, 9, 6, 17]

print(num)
maximo = num[0]
for num in num:
    if num > maximo:
        maximo = num
print(f'El número máximo es {maximo}')

print()

# Dada una lista de números enteros, cuenta cuántos números son positivos.
números = [-3, 5, -7, 2, -8, 10, -4, 6]

print(números)
positivos = 0
for num in números:
    if num > 0:
        positivos += 1
print(f'Hay {positivos} números positivos')
print()

# Dada una lista, invierte el orden de los elementos sin usar métodos como reverse().
numeros = [1, 2, 3, 4, 5]

print(numeros)
print("Numeros invertidos")
numeros_invertidos = []
for num in numeros:
    numeros_invertidos.insert(0, num)
print(numeros_invertidos)

print()

# Dada una lista de números, encuentra y muestra la media (promedio) de los elementos de la lista.
numeros = [4, 7, 2, 9, 3, 8, 5]

print(numeros)
suma = 0
for num in numeros:
    suma += num
media = suma / len(numeros)
print(f'La media de la lista de numeros es {media}')

