from tkinter import *


class MatrixTable(Frame):
    def __init__(self, parent, matrix):
        Frame.__init__(self, parent)

        self.rows = len(matrix)
        self.columns = len(matrix[0])

        for row in range(self.rows):
            for column in range(self.columns):
                entryText = StringVar()
                e = Entry(self, textvariable=entryText, state=DISABLED)
                entryText.set(('%f' % matrix[row][column]).rstrip('0').rstrip('.'))
                e.grid(row=row, column=column, stick="nsew")
        for column in range(self.columns):
            self.grid_columnconfigure(column, weight=1)
        self.grid_rowconfigure(self.rows, weight=1)


class MatrixInputTable(Frame):
    def __init__(self, parent, rows, columns):
        Frame.__init__(self, parent)

        self._entry = {}
        self.rows = rows
        self.columns = columns

        vcmd = (self.register(self.validate), "%P")

        for row in range(self.rows):
            for column in range(self.columns):
                index = (row, column)
                e = Entry(self, validate="key", validatecommand=vcmd)
                e.grid(row=row, column=column, stick="nsew")
                self._entry[index] = e
        for column in range(self.columns):
            self.grid_columnconfigure(column, weight=1)
        self.grid_rowconfigure(rows, weight=1)

    def get(self):
        result = []
        for row in range(self.rows):
            current_row = []
            for column in range(self.columns):
                index = (row, column)
                current_row.append(float(self._entry[index].get()))
            result.append(current_row)
        return result

    def validate(self, P):
        if P.strip() == "":
            return True

        if P == "-":
            return True

        try:
            f = float(P)
        except ValueError:
            self.bell()
            return False
        return True


class MatrixInputFrame(Frame):
    def __init__(self, parent, rows, cols):
        Frame.__init__(self, parent)
        self.table = MatrixInputTable(self, rows, cols)
        self.table.pack(side=TOP)

    def on_submit(self):
        print(self.table.get())

    def get_matrix(self):
        return self.table.get()
