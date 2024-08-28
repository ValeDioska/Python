#Elabora una lista de numeros (7 números en la lista) y modifica dos elementos de esta lista
num = ['1', '13', '22', '33', '47', '53', '69']
print(num)

print("Resultado cambiado")
    #Cambio de números
num [0] = '90'
print(num)
print()

#Elabora una lista de frutas de tu gusto y que el usuario pueda cambiar una de las frutas y que se guarde en la lista nueva
frut = ['Mango', 'Fresa', 'Uva', 'Piña', 'Manzana', 'Platano']
print("Esta es la lista de frutas: ")
for i, fruta in enumerate(frut):
    print(f"{i+1}. {fruta}")

cambio_frut = int(input("¿Cuál te gustaría cambiar? (ingresa el número de la fruta) ")) - 1
nueva_frut = input("¿Cuál es la nueva? ")

frut[cambio_frut] = nueva_frut
print(frut)

print()

#Realiza una lista que contenga elementos de diferentes tipos (números y un valor boleano) con un For mostrará lo que contiene
# Crear una lista con elementos de diferentes tipos
lista = [1, 2, 3, True, 4.5, "Hola", False]

for elemento in lista:
    print(elemento)

