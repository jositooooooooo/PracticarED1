import tkinter as tk

from models.model import Polinomio
from views.view import View
from controllers.controller import Controller


def main():
    "Función principal que inicializa el modelo, la vista y el controlador."
    root = tk.Tk()
    root.title("Polinomio - MVC")

    model = Polinomio()
    view = View(root)
    controller = Controller(view, model)

    root.mainloop()


if __name__ == "__main__":
    main()