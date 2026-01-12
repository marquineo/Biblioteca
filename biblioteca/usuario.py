class Usuario:
    def __init__(self, id, nombre, max_prestamos=3):

        if max_prestamos < 1:
            raise ValueError("Minimo 1 prestamo maximo")
        
        self.id = id
        self.nombre = nombre
        self.max_prestamos = max_prestamos

    def __str__(self):
        return f"ID Usuario: {self.id} | Nombre: {self.nombre} | max. Préstamos a la vez: {self.max_prestamos}"
