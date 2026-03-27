from prestamo import Prestamo

class PrestamoFactory:
    """
    Patrón Factory:
    Esta clase se encarga de crear objetos Prestamo.
    """

    @staticmethod
    def crear_prestamo(libro, usuario, fecha_inicio, dias_maximos=10):
        """
        Método estático que crea y devuelve un nuevo préstamo.

        Parámetros:
        - libro: objeto Libro que se va a prestar
        - usuario: objeto Usuario que realiza el préstamo
        - fecha_inicio: fecha en la que comienza el préstamo
        - dias_maximos: duración del préstamo (por defecto 10 días)

        Se utiliza @staticmethod porque no depende del estado de la clase.
        """

        # Se crea directamente el objeto Prestamo con los datos recibidos
        return Prestamo(libro, usuario, fecha_inicio, dias_maximos)