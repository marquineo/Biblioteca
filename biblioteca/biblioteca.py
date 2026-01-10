from Libro import Libro
from Usuario import Usuario
from Prestamo import Prestamo
from datetime import date, datetime

class Biblioteca:
    def __init__(self):
        self.usuarios: list[Usuario] = []
        self.libros: list[Libro] = []
        self.prestamos_activos: list[Prestamo] = []
        self.prestamos_vencidos = []
        
        # Usuarios y libros por defecto
        self._cargar_datos_por_defecto()

    def _cargar_datos_por_defecto(self):
        # 2 Usuarios
        self.registrar_usuario(Usuario("U001", "Ana García"))
        self.registrar_usuario(Usuario("U002", "Carlos Pérez"))
        # 5 Libros
        self.registrar_libro(Libro("978-1", "Cien años de soledad", "G. Márquez"))
        self.registrar_libro(Libro("978-2", "El Principito", "Saint-Exupéry"))
        self.registrar_libro(Libro("978-3", "1984", "George Orwell"))
        self.registrar_libro(Libro("978-4", "Harry Potter", "J.K. Rowling"))
        self.registrar_libro(Libro("978-5", "Don Quijote", "Cervantes"))

    def registrar_libro(self, libro: Libro):
        self.libros.append(libro)

    def registrar_usuario(self, usuario: Usuario):
        if not self.buscar_usuario(usuario.id):
            self.usuarios.append(usuario)
            return True
        return False

    def buscar_usuario(self, id_buscado):
        """Busca un usuario comparando directamente el atributo id"""
        for user in self.usuarios:
            if user.id == id_buscado:
                return user
        return None

    def buscar_libro(self, isbn):
        for libro in self.libros:
            if libro.isbn == isbn:
                return libro
        return None

    def prestar_libro(self, isbn, id_usuario, fecha_inicio):
        libro = self.buscar_libro(isbn)
        usuario = self.buscar_usuario(id_usuario)

        # 1. Verificar si el libro existe y está disponible
        if not libro:
            raise RuntimeError("El libro no está disponible o no existe")
        
        # 2. Verificar si el usuario existe
        if not usuario:
            raise RuntimeError("Usuario no encontrado")

        # 3. Verificar límite de préstamos del usuario
        contador = 0
        for prestamo in self.prestamos_activos:
            if prestamo.usuario == usuario:
                contador = contador + 1
        if contador >= usuario.max_prestamos:
            raise RuntimeError("El usuario ya tiene demasiados libros prestados")

        # Crear préstamo
        nuevo_prestamo = Prestamo(libro, usuario, fecha_inicio)
        
        self.prestamos_activos.append(nuevo_prestamo)
        self.libros.remove(libro)
        
        return nuevo_prestamo

    def devolver_libro(self, isbn, fecha_devolucion):
        prestamo_encontrado = None
        for p in self.prestamos_activos:
            if p.libro.isbn == isbn:
                prestamo_encontrado = p
                break
        
        if not prestamo_encontrado:
            return None

        prestamo_encontrado.devolver(fecha_devolucion)
        self.prestamos_activos.remove(prestamo_encontrado)
        self.prestamos_vencidos.append(prestamo_encontrado)
        self.libros.append(prestamo_encontrado.libro)
        
        return prestamo_encontrado

    def mostrar_info(self):
        print(f"Libros: {len(self.libros)} | Usuarios: {len(self.usuarios)}")

    def mostrar_prestamos_activos(self):
        print("======PRÉSTAMOS ACTIVOS======")
        for item in self.prestamos_activos:
            print(item)