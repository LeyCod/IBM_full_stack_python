import random

#Crea una matriz de NxN y le asigna un numero aleatorio a sus valores usando "list comprehencion".
def matrix_generator(input_number):
    matrix = [[random.randint(0, 9) for _ in range(input_number)] for _ in range(input_number)]
    return matrix

#Imprime las filas de la matriz generada.
def matrix_printer(matrix):
    for row in matrix:
        print(row)

#Suma los valores de las filas.
def rows_sum(matrix):
    return [sum(row) for row in matrix]

#Suma los valores de las columnas.
def columns_sum(matrix):
    return [sum(row[i] for row in matrix) for i in range(len(matrix[0]))]

# En la funcion main() encapsulamos la logica principal, utilizando las funciones antes creadas e iniciando su ejecicion. 
# En este caso utilizando tambien un try y except para manejar los posibles errores
def main():
    try:
        input_number = int(input("Ingrese un numero entero mayor a cero: "))
        if input_number <= 0:
            print("El tamaño de la matriz debe ser mayor que cero")
            return

        matrix = matrix_generator(input_number)
        print("Matriz generada:")
        matrix_printer(matrix)

        row_sum = rows_sum(matrix)
        column_sum = columns_sum(matrix)

        print("\nSuma de cada fila:")
        print(row_sum)

        print("\nSuma de cada columna:")
        print(column_sum)

    except ValueError:
        print("Error: Ingrese un número entero válido para generar la matriz.")

if __name__ == "__main__":
    main()