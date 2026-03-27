from abc import ABC, abstractmethod, ABCMeta


class ValidacionModelo(ABCMeta):
    """
    Metaclase que valida que las clases del modelo tengan ciertos atributos.
    Se ejecuta en tiempo de creación de la clase (no de instancia).
    """

    def __new__(cls, name, bases, dct):

        # Evitamos validar la clase base Persona
        if name != "Persona":

            # Comprobamos si 'id' está definido en la clase o en sus padres
            if "id" not in dct and not any("id" in base.__dict__ for base in bases):
                print(f"[VALIDACION] {name} debería tener atributo id")

        return super().__new__(cls, name, bases, dct)


class Persona(ABC, metaclass=ValidacionModelo):
    """
    Clase abstracta base para Usuario (y posibles futuras entidades).
    """

    def __init__(self, id, nombre):
        self.id = id
        self.nombre = nombre

    @abstractmethod
    def mostrar_info(self):
        pass