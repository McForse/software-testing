class Matrix:

    def __init__(self, matrix):
        self.__matrix = matrix
        self.__row = len(matrix)
        self.__col = self.__determine_col()

    def get_matrix(self):
        return self.__matrix

    def get_row_count(self):
        return self.__row

    def get_col_count(self):
        return self.__col

    def __determine_col(self):
        if self.__row == 0:
            return 0
        col = len(self.__matrix[0])
        for i in range(1, self.__row):
            if col != len(self.__matrix[i]):
                raise RuntimeError('Некорректная инициализация матрицы')
        return col

    def __dimension_equals(self, other):
        if self.__row == other.get_row_count() and self.__col == other.get_col_count():
            return True
        return False

    def sum(self, other):
        if self.__dimension_equals(other):
            return [[self.__matrix[i][j] + other.get_matrix()[i][j] for j in range(self.__col)] for i in
                    range(self.__row)]
        raise RuntimeError('Разная размерность матриц')

    def __add__(self, other):
        return self.sum(other)

    def sub(self, other):
        if self.__dimension_equals(other):
            return [[self.__matrix[i][j] - other.get_matrix()[i][j] for j in range(self.__col)] for i in
                    range(self.__row)]
        raise RuntimeError('Разная размерность матриц')

    def __sub__(self, other):
        return self.sub(other)

    def mul_by_number(self, number):
        return [[i * number for i in self.__matrix[_row]] for _row in range(self.__row)]

    def mul(self, other):
        if self.__col == other.get_row_count():
            return [
                [sum([self.__matrix[i][k] * other.get_matrix()[k][j] for k in range(other.get_row_count())]) for j in
                 range(other.get_col_count())] for i in range(self.__row)]
        raise RuntimeError('Число столбцов у первой матрицы не равно числу строк у второй')

    def __mul__(self, other):
        if isinstance(other, int):
            return self.mul_by_number(other)
        return self.mul(other)

    def transpose(self):
        return [[self.__matrix[i][j] for i in range(self.__row)] for j in range(self.__col)]

    def __eq__(self, other):
        if type(other) is Matrix:
            other_matrix = other.get_matrix()
        else:
            other_matrix = Matrix(other).get_matrix()
        return self.__matrix == other_matrix


class CooSparseMatrix:

    def __init__(self, matrix):
        self.__row = len(matrix)
        self.__col = len(matrix[0])
        for i in range(1, self.__row):
            if self.__col != len(matrix[i]):
                raise RuntimeError('Некорректная инициализация матрицы')

        self.__rows, self.__cols, self.__data = self.to_coo(matrix)

    def to_coo(self, matrix):
        rows = []
        cols = []
        data = []

        for i in range(self.__row):
            for j in range(self.__col):
                if matrix[i][j] != 0:
                    rows.append(i)
                    cols.append(j)
                    data.append(matrix[i][j])

        return rows, cols, data

    def transpose(self):
        tmp = self.__row
        self.__row = self.__col
        self.__col = tmp
        tmp = self.__rows
        self.__rows = self.__cols
        self.__cols = tmp
        return self

    def to_matrix(self):
        matrix = [[0 for _ in range(self.__col)] for _ in range(self.__row)]
        for i in range(len(self.__rows)):
            matrix[self.__rows[i]][self.__cols[i]] = self.__data[i]

        return matrix
