class Polinomio:

    def __init__(self):
        self._terminos = {}

    def agregar_termino(self, coeficiente, exponente):
        "Agrega un término al polinomio. Si el exponente ya existe, se reemplaza el coeficiente."
        if exponente < 0:
            raise ValueError("Exponente inválido")

        self._terminos[exponente] = coeficiente

    def __str__(self):
        "Devuelve una representación en cadena del polinomio."
        if not self._terminos:
            return "0"

        piezas = []

        for exp in sorted(self._terminos, reverse=True):
            coef = self._terminos[exp]

            if exp == 0:
                piezas.append(f"{coef:g}")
            elif exp == 1:
                piezas.append(f"{coef:g}x")
            else:
                piezas.append(f"{coef:g}x^{exp}")

        return " + ".join(piezas)