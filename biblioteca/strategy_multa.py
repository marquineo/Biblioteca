class EstrategiaMulta:
    def calcular(self, dias_retraso):
        """
        Se asegura de que la funcion calcular() se implementa
        """
        raise NotImplementedError("Debe implementar calcular()")

class MultaEstandar(EstrategiaMulta):
    def calcular(self, dias):
        return dias * 10

class MultaReducida(EstrategiaMulta):
    def calcular(self, dias):
        return dias * 5

class MultaProgresiva(EstrategiaMulta):
    def calcular(self, dias):
        if dias <= 5:
            return dias * 5
        return 5 * 5 + (dias - 5) * 15