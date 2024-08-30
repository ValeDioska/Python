# Escribe un programa que tome dos matrices de igual tamaño (matrices bidimensionales) y 
# devuelva una nueva matriz que sea la suma de las dos matrices originales.

matrix_1 = [[1,2,3], 
            [4,5,6], 
            [7,8,9]]
print(f'Esta es la primera matriz {matrix_1}')
print()
matrix_2 = [[30,31,32],
            [33,34,35],
            [36,37,38]]
print(f'Esta es la segunda matriz {matrix_2}')
print()

resultado = [[0,0,0],
             [0,0,0],
             [0,0,0]]

for i in range (len(matrix_1)):
    for j in range (len(matrix_2)):
        resultado [i][j] = matrix_1 [i][j] + matrix_2 [i][j]

print(f'Esta es la suma de las dos primeras: {resultado}')
print("Fin del programa")
print()
# Crea un programa que multiplique dos matrices de tamaño adecuado. 
# Recuerda que para multiplicar matrices, el número de columnas de la primera debe coincidir con el número de filas de la segunda
matrix_1 = [[80,81,82], 
            [83,84,85], 
            [86,87,88]]
print(f'Esta es la primera matriz {matrix_1}')
print()
matrix_2 = [[11,12,13],
            [14,15,16],
            [17,18,19]]
print(f'Esta es la segunda matriz {matrix_2}')
print()

resultado = [[0,0,0],
             [0,0,0],
             [0,0,0]]

for i in range (len(matrix_1)):
    for j in range (len(matrix_2)):
        resultado [i][j] = matrix_1 [i][j] * matrix_2 [i][j]

print(f'Esta es la multipicación de las dos primersas: {resultado}')
print("Fin del programa")
print()

# Tome una matriz y devuelva su transpuesta (intercambiar filas por columnas)
# Definimos la matriz original
matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]

print(matrix)
matrixtrans = [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]
print("La matriz transpuesta es:")
for fila in matrixtrans:
    print(fila)
print("Fin del programa")
print()

# Un cuadrado mágico es una matriz en la que la suma de cada fila, columna y diagonal es la misma. 
# Escribe un programa que determine si una matriz dada es un cuadrado mágico.
def is_magic_square(matrix):
    n = len(matrix)
    sum_row = sum(matrix[0])
    sum_diagonal1 = 0
    sum_diagonal2 = 0

    for i in range(n):
        if sum(matrix[i]) != sum_row:
            return False
        sum_diagonal1 += matrix[i][i]
        sum_diagonal2 += matrix[i][n - i - 1]

    for j in range(n):
        if sum(matrix[i][j] for i in range(n)) != sum_row:
            return False

    if sum_diagonal1 != sum_row or sum_diagonal2 != sum_row:
        return False

    return True

# Matrices a evaluar
matrix1 = [[1, 2, 3],
           [4, 5, 6],
           [7, 8, 9]]

matrix2 = [[9, 8, 7],
           [6, 5, 4],
           [3, 2, 1]]

matrix3 = [[2, 7, 6],
           [9, 5, 1],
           [4, 3, 8]]

# Imprimir matrices
print(f'Esta es la primera matriz:\n{matrix1}')
print(f'Esta es la segunda matriz:\n{matrix2}')
print(f'Esta es la tercera matriz:\n{matrix3}')
print()

# Verificar si son cuadrados mágicos
print(f"¿Matriz 1 es un cuadrado mágico?: {is_magic_square(matrix1)}")
print(f"¿Matriz 2 es un cuadrado mágico?: {is_magic_square(matrix2)}")
print(f"¿Matriz 3 es un cuadrado mágico?: {is_magic_square(matrix3)}")

print("Fin del programa")
