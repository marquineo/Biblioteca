class EstrategiaMulta:
    def calcular(self, dias_retraso):
        raise NotImplementedError("Debe implementar calcular()")

class MultaEstandar(EstrategiaMulta):
    def calcular(self, dias_retraso):
        return dias_retraso * 10