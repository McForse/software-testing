from tkinter import *

from matrix_calculator.main import Matrix
from ui.MatrixFrame import MatrixTable, MatrixInputFrame

bg = '#ececec'


class TransposeTab(Frame):
    def __init__(self):
        Frame.__init__(self, background=bg)
        self.result_frame = Frame(self, background=bg)
        self.matrix = None
        self.result_matrix = None

        self.start()

    def solve(self):
        if self.result_matrix is not None:
            self.result_matrix.destroy()

        result_matrix = Matrix(self.matrix.get_matrix()).transpose()

        self.result_matrix = MatrixTable(self.result_frame, result_matrix)
        self.result_frame.pack(anchor='w')
        self.result_matrix.pack(side=LEFT, padx=5, pady=5)

    def start(self):
        frame2 = Frame(self, background=bg)
        frame2.pack(anchor='w')

        matrix_size_label = Label(frame2)
        matrix_size_label.configure(text='Размер матрицы:', background=bg)
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
        matrix_label = Label(frame3)
        matrix_label.configure(text='Матрица:', background=bg)
        matrix_label.pack(side=TOP, padx=5, pady=5)

        self.matrix = MatrixInputFrame(frame3, *[int(i) for i in matrix_size_variable.get().split("x")])
        self.matrix.pack(side=TOP, padx=5, pady=5)

        frame4 = Frame(self, background=bg)
        frame4.pack(anchor='w')

        def change_dimension(*args):
            self.matrix.destroy()
            self.matrix = MatrixInputFrame(frame3, *[int(i) for i in matrix_size_variable.get().split("x")])
            self.matrix.pack(side=LEFT, padx=5, pady=5)

        matrix_size_variable.trace("w", change_dimension)

        solve_button = Button(self, text="Вычислить", command=self.solve, highlightbackground=bg, padx=5, pady=5)
        solve_button.pack()
