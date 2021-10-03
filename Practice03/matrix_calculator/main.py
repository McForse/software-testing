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
                raise RuntimeError
        return col

    def sum(self, other):
        return [[self.__matrix[i][j] + other.get_matrix()[i][j] for j in range(self.__col)] for i in range(self.__row)]

    def __add__(self, other):
        return self.sum(other)

    def sub(self, other):
        return [[self.__matrix[i][j] - other.get_matrix()[i][j] for j in range(self.__col)] for i in range(self.__row)]

    def __sub__(self, other):
        return self.sub(other)

    def mul_by_number(self, number):
        return [[i * number for i in self.__matrix[_row]] for _row in range(self.__row)]

    def mul(self, other):
        return [[sum([self.__matrix[i][k] * other.get_matrix()[k][j] for k in range(other.get_row_count())]) for j in
                 range(other.get_col_count())] for i in range(self.__row)]

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
