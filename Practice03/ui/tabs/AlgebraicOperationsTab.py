from tkinter import *

from matrix_calculator.main import Matrix
from ui.MatrixFrame import MatrixInputFrame, MatrixTable

bg = '#ececec'


class AlgebraicOperationsTab(Frame):
    def __init__(self):
        Frame.__init__(self, background=bg)
        self.result_frame = Frame(self, background=bg)

        self.operation = None
        self.matrix_a = None
        self.matrix_b = None
        self.result_matrix = None

        self.start()

    def solve(self):
        if self.result_matrix is not None:
            self.result_matrix.destroy()

        if self.operation == "Сложение":
            result_matrix = Matrix(self.matrix_a.get_matrix()) + Matrix(self.matrix_b.get_matrix())
        elif self.operation == "Вычитание":
            result_matrix = Matrix(self.matrix_a.get_matrix()) - Matrix(self.matrix_b.get_matrix())
        else:
            result_matrix = Matrix(self.matrix_a.get_matrix()) * Matrix(self.matrix_b.get_matrix())

        self.result_matrix = MatrixTable(self.result_frame, result_matrix)
        self.result_frame.pack(anchor='w')
        self.result_matrix.pack(side=LEFT, padx=5, pady=5)

    def start(self):
        frame1 = Frame(self, background=bg)
        frame1.pack(anchor='w')

        operation_label = Label(frame1)
        operation_label.configure(text='Операция:', background=bg)
        operation_label.pack(side=LEFT, padx=5, pady=5)

        operation_options = ["Сложение", "Вычитание", "Умножение"]
        operation_variable = StringVar(frame1)
        operation_variable.set(operation_options[0])
        operation_option_menu = OptionMenu(frame1, operation_variable, *operation_options)
        operation_option_menu.config(background=bg)
        operation_option_menu.pack(side=LEFT, padx=5, pady=5)

        def set_operation(*args):
            self.operation = operation_variable.get()

        operation_variable.trace("w", set_operation)

        frame2 = Frame(self, background=bg)
        frame2.pack(anchor='w')

        matrix_size_label = Label(frame2)
        matrix_size_label.configure(text='Размер матриц:', background=bg)
        matrix_size_label.pack(side=LEFT, padx=5, pady=5)
        matrix_sizes = [[1, 1], [2, 2], [3, 3], [4, 4]]
        matrix_sizes_options = ['x'.join([str(i) for i in _size]) for _size in matrix_sizes]
        matrix_size_variable = StringVar(frame2)
        matrix_size_variable.set(matrix_sizes_options[2])
        matrix_size_options_menu = OptionMenu(frame2, matrix_size_variable, *matrix_sizes_options)
        matrix_size_options_menu.config(background=bg)
        matrix_size_options_menu.pack(side=LEFT, padx=5, pady=5)

        frame3 = Frame(self, background=bg)
        frame3.pack(anchor='w')
        matrix_a_label = Label(frame3)
        matrix_a_label.configure(text='Матрица А:', background=bg)
        matrix_a_label.pack(side=TOP, padx=5, pady=5)

        self.matrix_a = MatrixInputFrame(frame3, *[int(i) for i in matrix_size_variable.get().split("x")])
        self.matrix_a.pack(side=TOP, padx=5, pady=5)

        frame4 = Frame(self, background=bg)
        frame4.pack(anchor='w')
        matrix_b_label = Label(frame4)
        matrix_b_label.configure(text='Матрица Б:', background=bg)
        matrix_b_label.pack(side=TOP, padx=5, pady=5)

        self.matrix_b = MatrixInputFrame(frame4, *[int(i) for i in matrix_size_variable.get().split("x")])
        self.matrix_b.pack(side=LEFT, padx=5, pady=5)

        def change_dimension(*args):
            self.matrix_a.destroy()
            self.matrix_a = MatrixInputFrame(frame3, *[int(i) for i in matrix_size_variable.get().split("x")])
            self.matrix_a.pack(side=LEFT, padx=5, pady=5)

            self.matrix_b.destroy()
            self.matrix_b = MatrixInputFrame(frame4, *[int(i) for i in matrix_size_variable.get().split("x")])
            self.matrix_b.pack(side=LEFT, padx=5, pady=5)

        matrix_size_variable.trace("w", change_dimension)

        solve_button = Button(self, text="Вычислить", command=self.solve, highlightbackground=bg, padx=5, pady=5)
        solve_button.pack()
