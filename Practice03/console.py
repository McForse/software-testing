from matrix_calculator.main import Matrix


def matrix_dimension_input(prompt="Введите размерность матриц (2 3): "):
    try:
        dimension = [int(i) for i in input(prompt).split()]
        if len(dimension) != 2:
            raise ValueError
        return dimension
    except ValueError:
        raise RuntimeError('Некорекный ввод размерности')

def matrix_input(rows, cols):
    return [[float(n) for n in input().split()] for _row in range(int(rows))]

def print_matrix(matrix):
    for row in matrix:
        for i in row:
            print(int(i), end=" ")
        print()

def main():
    print("Матричный калькулятор")

    while True:
        print("\nДоступные операции:")
        print(
            "1. Сложение  матриц\n2. Вычитание матриц\n3. Умножение матрицы на число\n4. Умножение матриц\n5. Транспонирование матрицы\n0. Выход")
        choice = input("Выберете операцию: ")

        if choice == "1":
            dimension = matrix_dimension_input()
            print("Введите данные перовой матрицы:")
            matrix_a = Matrix(matrix_input(dimension[0], dimension[1]))
            print("Введите данные второй матрицы:")
            matrix_b = Matrix(matrix_input(dimension[0], dimension[1]))
            print("Результат сложения:")
            print_matrix(matrix_a.sum(matrix_b))

        elif choice == "2":
            dimension = matrix_dimension_input()
            print("Введите данные перовой матрицы:")
            matrix_a = Matrix(matrix_input(dimension[0], dimension[1]))
            print("Введите данные второй матрицы:")
            matrix_b = Matrix(matrix_input(dimension[0], dimension[1]))
            print("Результат вычитания:")
            print_matrix(matrix_a.sub(matrix_b))

        elif choice == "3":
            dimension = matrix_dimension_input()
            print("Введите данные матрицы:")
            matrix = Matrix(matrix_input(dimension[0], dimension[1]))
            number = int(input("Введите число, на которое хотите умножить матрицу: "))
            print("Результат умножения на число:")
            print_matrix(matrix.mul_by_number(number))

        elif choice == "4":
            dimension_a = matrix_dimension_input("Введите размерность первой матрицы: ")
            print("Введите данные перовой матрицы:")
            matrix_a = Matrix(matrix_input(dimension_a[0], dimension_a[1]))
            dimension_b = matrix_dimension_input("Введите размерность второй матрицы: ")
            print("Введите данные второй матрицы:")
            matrix_b = Matrix(matrix_input(dimension_b[0], dimension_b[1]))
            print("Результат умножения:")
            print_matrix(matrix_a.mul(matrix_b))

        elif choice == "5":
            dimension = matrix_dimension_input()
            print("Введите данные матрицы:")
            matrix = Matrix(matrix_input(dimension[0], dimension[1]))
            print("Результат транспонирования:")
            print_matrix(matrix.transpose())

        else:
            break


if __name__ == "__main__":
    main()
