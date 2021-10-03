from tkinter import *
from tkinter import ttk

from ui.tabs.AlgebraicOperationsTab import AlgebraicOperationsTab
from ui.tabs.TransposeTab import TransposeTab


class MatrixCalculatorUI:

    def __init__(self):
        self.window = Tk()
        self.tab_parent = ttk.Notebook(self.window)
        self.tab1 = AlgebraicOperationsTab()
        self.tab2 = TransposeTab()

    def start(self):
        self.window.title("Матричный калькулятор")
        self.window.geometry("500x700")

        self.tab_parent.add(self.tab1, text="Алгебраические операции")
        self.tab_parent.add(self.tab2, text="Транспонирование")

        self.tab_parent.pack(expand=1, fill='both')

        mainloop()


if __name__ == '__main__':
    ui = MatrixCalculatorUI()
    ui.start()
