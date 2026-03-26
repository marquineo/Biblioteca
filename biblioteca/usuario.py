from persona import Persona

class Usuario(Persona):
    def __init__(self, id, nombre, max_prestamos=3):
        super().__init__(id, nombre)

        if max_prestamos < 1:
            raise ValueError("Minimo 1 prestamo maximo")
        
        self.max_prestamos = max_prestamos

    def mostrar_info(self):
        return f"ID Usuario: {self.id} | Nombre: {self.nombre} | max. Préstamos: {self.max_prestamos}"

    def __str__(self):
        return self.mostrar_info()

    def __call__(self):
        return self.id