class Controller:

    def __init__(self, view, model):
        self.view = view
        self.model = model

        self.view.boton_agregar.config(
            command=self.agregar_termino
        )

    def agregar_termino(self):
        coeficiente = self.view.obtener_coeficiente()
        exponente = self.view.obtener_exponente()

        self.model.agregar_termino(
            coeficiente,
            exponente
        )

        self.view.mostrar_polinomio(
            self.model
        )