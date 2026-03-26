from prestamo import Prestamo

class PrestamoFactory:

    @staticmethod
    def crear_prestamo(libro, usuario, fecha_inicio, dias_maximos=10):
        return Prestamo(libro, usuario, fecha_inicio, dias_maximos)