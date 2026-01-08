from Libro import Libro
from Usuario import Usuario
from Prestamo import Prestamo

from datetime import date
class Biblioteca:
    hoy = date.today()
    def __init__(self):
        self.usuarios: list[Usuario] = []
        self.libros: list[Libro] = []
        self.prestamos_activos: list[Prestamo] = []
        self.prestamos_vencidos = []

    def registrar_libro(self,ISBN,titulo,autor):
        libro = Libro(ISBN,titulo,autor)
        self.libros.append(libro)

    def registrar_usuarios(self,identificador,nombre):
        user = Usuario(identificador,nombre)
        self.usuarios.append(user)

    def crear_prestamo(self,inicio,fin,libro: Libro,usuario: Usuario,):
        prestamo = Prestamo(inicio,fin,libro,usuario)
        self.prestamos_activos.append(prestamo)
        self.libros.remove(libro)

    def devolver_libro(self,prestamo: Prestamo):
        for item in self.prestamos_activos:
            if item == prestamo:
                item.devolver(self.hoy)
                self.prestamos_vencidos.append(item)
                self.prestamos_activos.remove(item)

    def is_prestamos_activos(self):
        print("Prestamos activos:")
        for item in self.prestamos_activos:
            print(item)