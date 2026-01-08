class Usuario:
    def __init__(self, identificador, nombre):
        self.identificador = identificador
        self.nombre = nombre
        self.PRESTAMOS_MAX = 3

    def __str__(self):
        return f"ID Usuario: {self.identificador} | Nombre: {self.nombre}"
