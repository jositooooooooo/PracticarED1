class Controller:

    def __init__(self, view, model):
        "Controlador que conecta la vista y el modelo."
        self.view = view
        self.model = model

        self.view.boton_agregar.config(
            command=self.agregar_termino
        )

    def agregar_termino(self):
        "Agrega un término al polinomio y actualiza la vista."
        coeficiente = self.view.obtener_coeficiente()
        exponente = self.view.obtener_exponente()

        self.model.agregar_termino(
            coeficiente,
            exponente
        )

        self.view.mostrar_polinomio(
            self.model
        )