class EstrategiaMulta:
    def calcular(self, dias_retraso):
        """
        Se asegura de que la funcion calcular() se implementa
        """
        raise NotImplementedError("Debe implementar calcular()")

class MultaEstandar(EstrategiaMulta):
    def calcular(self, dias_retraso):
        """
        Calcula la multa
        """
        return dias_retraso * 10