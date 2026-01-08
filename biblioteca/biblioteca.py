from Libro import Libro
from Usuario import Usuario
from Prestamo import Prestamo
from datetime import date, datetime


class Biblioteca:
    hoy = date.today()

    def __init__(self):
        self.usuarios: list[Usuario] = []
        self.libros: list[Libro] = []
        self.prestamos_activos: list[Prestamo] = []
        self.prestamos_vencidos = []

    def registrar_libro(self, ISBN, titulo, autor):
        """Registra un libro nuevo en la biblioteca"""
        libro = Libro(ISBN, titulo, autor)
        self.libros.append(libro)

    def buscar_usuario(self, id):
        """Busca un usuario por id"""
        for item in self.usuarios:
            if item.identificador == id:
                return item
        return False

    def buscar_libro(self, isbn):
        """Busca un libro por isbn"""
        for item in self.libros:
            if item.isbn == isbn:
                return item
        return False

    def registrar_usuarios(self, identificador, nombre):
        """Registra un nuevo usuario en la biblioteca"""
        if not self.buscar_usuario(identificador):
            user = Usuario(identificador, nombre)
            self.usuarios.append(user)
        else:
            return False

    def crear_prestamo(
        self,
        fin,
        isbn,
        id,
    ):
        """Crea un prestamo y elimina el libro prestado"""
        libro = self.buscar_libro(isbn)
        usuario = self.buscar_usuario(id)
        if libro == False or usuario == False:
            raise ValueError("No se encontro libro o usuario")

        fecha_formato = "%d/%m/%Y"
        fecha_fin = datetime.strptime(fin, fecha_formato).date()
        prestamo = Prestamo(self.hoy, fecha_fin, libro, usuario)
        self.prestamos_activos.append(prestamo)
        self.libros.remove(libro)

    def devolver_libro(self, id, isbn):
        """Devuelve un prestamo moviendolo a la lista
        de prestamos_vencidos y agrega de nuevo el libro"""
        libro = self.buscar_libro(isbn)
        usu = self.buscar_usuario(id)
        for item in self.prestamos_activos:
            if item.usuario == usu and item.libro == libro:
                item.devolver(self.hoy)
                self.prestamos_vencidos.append(item)
                self.prestamos_activos.remove(item)
                self.libros.append(item.libro)

                if self.hoy > item.fin:
                    multa = item.calcular_multa()
                    print(f"El usuario debe abonar una cantidad de {multa}€ por retraso en la devolución")

    def mostrar_prestamos_activos(self):
        """Muestra los prestamos activos"""
        print("=== PRÉSTAMOS ===")
        for item in self.prestamos_activos:
            print(item)

    def mostrar_info(self):
        """Muestra los libros y usuarios de la biblioteca y su estado"""
        print("=== LIBROS ===")
        for libro in self.libros:
            print(libro)

        print("\n=== USUARIOS ===")
        for usuario in self.usuarios:
            print(usuario)