from abc import ABC, abstractmethod


class ValidacionModelo(type):

    def __new__(cls, name, bases, dct):

        if name != "Persona":
            if "id" not in dct and not any("id" in base.__dict__ for base in bases):
                print(f"[VALIDACION] {name} debería tener atributo id")

        return super().__new__(cls, name, bases, dct)


class Persona(ABC, metaclass=ValidacionModelo):
    def __init__(self, id, nombre):
        self.id = id
        self.nombre = nombre

    @abstractmethod
    def mostrar_info(self):
        pass