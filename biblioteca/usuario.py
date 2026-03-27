from persona import Persona

class Usuario(Persona):
    def __init__(self, id, nombre, max_prestamos=3):
        # Llamamos al constructor de Persona para inicializar id y nombre
        super().__init__(id, nombre)

        # Número máximo de préstamos simultáneos permitidos
        self.max_prestamos = max_prestamos

        # Lista donde se guardará el historial de préstamos del usuario
        self.historial: list = []

        # Validación: un usuario debe poder tener al menos 1 préstamo
        if max_prestamos < 1:
            raise ValueError("Minimo 1 prestamo maximo")
        
        # Reasignación final tras validación (evita valores inválidos)
        self.max_prestamos = max_prestamos

    def mostrar_info(self):
        """
        Devuelve una representación en texto del usuario.
        Se utiliza para mostrar información de forma clara por consola.
        """
        return f"ID Usuario: {self.id} | Nombre: {self.nombre} | max. Préstamos: {self.max_prestamos}"

    def __str__(self):
        """
        Permite imprimir directamente el objeto usuario con print(usuario)
        sin necesidad de llamar a mostrar_info().
        """
        return self.mostrar_info()

    def __call__(self):
        """
        Permite llamar al objeto como si fuera una función.
        Devuelve el ID del usuario.

        Se utiliza para simplificar comparaciones en búsquedas.
        """
        return self.id