import tkinter as tk


class View:

    def __init__(self, master):
        self.master = master

        self.master.title("Generador de Polinomio")

        self.label_coeficiente = tk.Label(
            master,
            text="Coeficiente:"
        )
        self.label_coeficiente.pack()

        self.entry_coeficiente = tk.Entry(master)
        self.entry_coeficiente.pack()

        self.label_exponente = tk.Label(
            master,
            text="Exponente:"
        )
        self.label_exponente.pack()

        self.entry_exponente = tk.Entry(master)
        self.entry_exponente.pack()

        self.boton_agregar = tk.Button(
            master,
            text="Agregar término"
        )
        self.boton_agregar.pack()

        self.label_polinomio = tk.Label(
            master,
            text="Polinomio: 0"
        )
        self.label_polinomio.pack()

    def obtener_coeficiente(self):
        return float(self.entry_coeficiente.get())

    def obtener_exponente(self):
        return int(self.entry_exponente.get())

    def mostrar_polinomio(self, polinomio):
        self.label_polinomio.config(
            text=f"Polinomio: {polinomio}"
        )