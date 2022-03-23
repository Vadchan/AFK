from tkinter import *
from tkinter.ttk import Combobox


class Screen:
    def __init__(self, elements):
        self.elements = elements

    def activate(self):
        for element in self.elements:
            element.lbl = Label(window, text="Выборка", font=("Arial Bold", 25))

            element.show()

    def deactivate(self):
        for element in self.elements:
            element.destroy()


class SecondScreen(Screen):
    def __init__(self):
        super().__init__([])


class FirstScreen(Screen):
    def __init__(self, window, next_screen):
        lbl = Label(window, text="Выборка", font=("Arial Bold", 25))
        lbl.grid(column=0, row=0)
        txt = Entry(window, width=30)
        txt.grid(column=1, row=0)
        txt.focus()
        combo = Combobox(window)
        combo['values'] = (1, 2, 3, 4, 5)
        combo.current(1)  # установите вариант по умолчанию
        combo.grid(column=2, row=0)
        btn = Button(window, text="Начать", command=self.clicked)
        btn.grid(column=3, row=0)
        self.next_screen = next_screen
        super().__init__((lbl, txt, combo, btn))

    def clicked(self):
        self.deactivate()
        self.next_screen.activate()


window = Tk()
window.title("csv")
window.geometry('1920x1080')
next_screen = SecondScreen()
first_screen = FirstScreen(window, next_screen)

window.mainloop()



