from Libro import Libro
from Usuario import Usuario
from datetime import date


class Prestamo:
    MULTA_POR_DIA = 2
    hoy = date.today()

    def __init__(
        self,
        inicio,
        fin,
        libro: Libro,
        usuario: Usuario,
        fecha_devolucion=None,
    ):
        if inicio > fin:
            raise ValueError("El inicio del prestamo no puede ser despues del final")

        if fecha_devolucion and fecha_devolucion < inicio:
            raise ValueError("La devolución no puede ser antes del inicio")

        self.inicio = inicio
        self.fin = fin
        self.fecha_devolucion = fecha_devolucion
        self.libro = libro
        self.usuario = usuario

    def is_activo(self) -> bool:
        """Retorna:
        False -> finalizado
        True -> activo"""
        if self.fecha_devolucion != None:
            return False
        return True

    def is_vencido(self) -> bool:
        if self.fecha_devolucion is not None:
            return False
        return date.today() > self.fin


    def calcular_multa(self) -> int:
        """Calcula la cantidad multada por dia de retraso"""
        dias_retraso = (self.fecha_devolucion - self.fin).days
        return dias_retraso * self.MULTA_POR_DIA
    
    def devolver(self,fecha:date):
        self.fecha_devolucion = fecha
