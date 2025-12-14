class GeneradorCodigo:
    def __init__(self):
        self.plantillas = {
            "promedio": self._generar_promedio,
            "suma": self._generar_suma,
            "validar_par": self._generar_validar_par
        }

    def generar(self, descripcion):
        descripcion = descripcion.lower()
        if "promedio" in descripcion:
            return self._generar_promedio()
        elif "suma" in descripcion:
            return self._generar_suma()
        elif "par" in descripcion:
            return self._generar_validar_par()
        else:
            return "# No se pudo generar el código. Descripción no reconocida."

    def _generar_promedio(self):
        return (
                "def calcular_promedio(lista):"
                " if not lista:"
                
                " return 0"
                
                " return sum(lista) / len(lista)"
            )

    def _generar_suma(self):
        return (
            "def sumar(a, b):"
            
            " return a + b"
        )

    def _generar_validar_par(self):
        return (
            "def es_par(numero):"
            
            " return numero % 2 == 0"
        )