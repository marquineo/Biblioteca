from abc import ABC, abstractmethod

class Persona(ABC):
    def __init__(self, id, nombre):
        self.id = id
        self.nombre = nombre

    @abstractmethod
    def mostrar_info(self):
        pass