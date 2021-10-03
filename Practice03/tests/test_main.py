from matrix_calculator.main import Matrix


def test_sum_matrix():
    """Проверка сложения матриц"""

    matrix_a = Matrix([
        [1, 2, 3],
        [5, 6, 7]
    ])

    matrix_b = Matrix([
        [4, 1, 5],
        [3, 5, 4]
    ])

    result = [
        [5, 3, 8],
        [8, 11, 11]
    ]

    assert result + result == 2 * result
    assert matrix_a.sum(matrix_b) == result
    assert matrix_a + matrix_b == result
    assert matrix_b.sum(matrix_a) == result
    assert matrix_b + matrix_a == result


def test_sub_matrix():
    """Проверка вычитания матриц"""

    matrix_a = Matrix([
        [15, 22, 52, 51, 10],
        [18, 16, 55, 81, 30],
        [13, 12, 34, 45, 12]
    ])

    matrix_b = Matrix([
        [19, 3, 31, 14, 12],
        [10, 66, 39, 15, 18],
        [22, 31, 15, 43, 44]
    ])

    result_a_sub_b = [
        [-4, 19, 21, 37, -2],
        [8, -50, 16, 66, 12],
        [-9, -19, 19, 2, -32]
    ]

    result_b_sub_a = [[-i for i in result_a_sub_b[_row]] for _row in range(len(result_a_sub_b))]

    assert matrix_a.sub(matrix_b) == result_a_sub_b
    assert matrix_a - matrix_b == result_a_sub_b
    assert matrix_b.sub(matrix_a) == result_b_sub_a
    assert matrix_b - matrix_a == result_b_sub_a

def test_mul_by_number_matrix():
    """Проверка умножения матрицы на число матриц"""

    matrix = Matrix([
        [4, 2, 5],
        [1, 3, 9],
        [10, 7, 11],
        [19, 6, 8]
    ])

    result_mul_by_3 = [
        [12, 6, 15],
        [3, 9, 27],
        [30, 21, 33],
        [57, 18, 24]
    ]

    result_mul_by_25 = [
        [100, 50, 125],
        [25, 75, 225],
        [250, 175, 275],
        [475, 150, 200]
    ]

    assert matrix.mul_by_number(3) == result_mul_by_3
    assert matrix * 3 == result_mul_by_3
    assert matrix.mul_by_number(25) == result_mul_by_25
    assert matrix * 25 == result_mul_by_25

def test_mul_matrix():
    """Проверка умножения матриц"""

    matrix_a = Matrix([
        [4, 1, 8],
        [5, 3, 7]
    ])

    matrix_b = Matrix([
        [9, 7, 2],
        [1, 0, 4],
        [2, 5, 3]
    ])

    result = [
        [53, 68, 36],
        [62, 70, 43],
    ]

    assert matrix_a.mul(matrix_b) == result
    assert matrix_a * matrix_b == result

def test_transpose_matrix():
    """Проверка транспонирования матрицы"""

    matrix_a = Matrix([
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
        [13, 14, 15, 16]
    ])

    matrix_b = Matrix([
        [10, 11, 12, 13]
    ])

    assert matrix_a.transpose() == [
        [1, 5, 9, 13],
        [2, 6, 10, 14],
        [3, 7, 11, 15],
        [4, 8, 12, 16]
    ]
    assert matrix_b.transpose() == [
        [10],
        [11],
        [12],
        [13]
    ]

def test_incorrect_matrix_init():
    """
    Проверка неправильной инициализации матрицы:
    неодинаковое число элементов в строке
    """
    try:
        Matrix([
            [1, 2],
            [3]
        ])
        assert False
    except RuntimeError:
        assert True

def test_incorrect_sum_sub_operations_matrix():
    """
    Проверка недопустимого сложения и вычитания матриц:
    матрицы имеют разную размерность
    """
    matrix_a = Matrix([
        [1, 2, 3]
    ])

    matrix_b = Matrix([
        [4, 1, 5],
        [3, 5, 4]
    ])

    try:
        matrix_a.sum(matrix_b)
        matrix_b + matrix_a
        matrix_a.sub(matrix_b)
        matrix_b - matrix_a
        assert False
    except RuntimeError:
        assert True

def test_incorrect_mul_matrix():
    """
    Проверка недопустимого умножения матриц:
    число столбцов у первой матрицы не равно числу строк у второй
    """
    matrix_a = Matrix([
        [4, 1, 2]
    ])

    matrix_b = Matrix([
        [9, 7, 2],
        [1, 0, 4]
    ])

    try:
        matrix_a.mul(matrix_b)
        matrix_a * matrix_b
        assert False
    except RuntimeError:
        assert True
