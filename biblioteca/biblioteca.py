from libro import Libro
from usuario import Usuario
from prestamo import Prestamo
from datetime import date, datetime
from prestamo_factory import PrestamoFactory


class Biblioteca:
    """
    Patrón FACADE:
    Esta clase simplifica la gestión del sistema de biblioteca,
    centralizando operaciones sobre libros, usuarios y préstamos.
    """
    MULTA_EUR_DIA = 10
    def __init__(self):
        self.usuarios: list[Usuario] = []
        self.libros: list[Libro] = []
        self.prestamos_activos: list[Prestamo] = []
        self.prestamos_vencidos: list[Prestamo] = []

        # Cargamos datos por defecto
        #self._cargar_datos_por_defecto()

    def _cargar_datos_por_defecto(self):
        # Usuarios por defecto
        self.registrar_usuario(Usuario("U001", "Ana García"))
        self.registrar_usuario(Usuario("U002", "Carlos Pérez"))
        # Libros por defecto
        self.registrar_libro(Libro("978-1", "Cien años de soledad", "G. Márquez"))
        self.registrar_libro(Libro("978-2", "El Principito", "Saint-Exupéry"))
        self.registrar_libro(Libro("978-3", "1984", "George Orwell"))
        self.registrar_libro(Libro("978-4", "Harry Potter", "J.K. Rowling"))
        self.registrar_libro(Libro("978-5", "Don Quijote", "Cervantes"))

    def __iter__(self):
        return iter(self.libros)

    def __getitem__(self, indice):
        return self.libros[indice]

    def __add__(self, libro):
        if not isinstance(libro, Libro):
            return NotImplemented
        self.libros.append(libro)
        return self

    def registrar_libro(self, libro: Libro):
        self.libros.append(libro)

    def registrar_usuario(self, usuario: Usuario) -> bool:
        """
        Recibe un usuario por parametro, y si no existe actualemtente
        lo registra.
        Retorma: True->Usuario registrado | False-> Usuario ya estaba registrado
        """
        if not self.buscar_usuario(usuario.id):
            self.usuarios.append(usuario)
            return True
        return False

    def buscar_usuario(self, id_buscado):
        """Busca un usuario comparando directamente el atributo id"""
        for user in self.usuarios:
            if user() == id_buscado:
                return user
        return None

    def buscar_libro(self, isbn):
        """Busca un libro comparando directamente el atributo isbn"""
        for libro in self.libros:
            if libro.isbn == isbn:
                return libro
        return None

    def prestar_libro(self, isbn, id_usuario, fecha_inicio):
        """Verifica que se cumplan las condiciones y crea el préstamo"""
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

        nuevo_prestamo = PrestamoFactory.crear_prestamo(libro, usuario, fecha_inicio)

        self.prestamos_activos.append(nuevo_prestamo)
        self.libros.remove(libro)

        return nuevo_prestamo

    def devolver_libro(self, isbn, fecha_devolucion):
        """
        Busca el préstamo pasado por parámetro y si lo encuentra lo devuelve y retorna
        retorna None si no lo encuentra
        """
        prestamo_encontrado = None
        for pres in self.prestamos_activos:
            if pres.libro.isbn == isbn:
                prestamo_encontrado = pres
                break

        if not prestamo_encontrado:
            return None

        prestamo_encontrado.devolver(fecha_devolucion)
        self.prestamos_activos.remove(prestamo_encontrado)
        self.prestamos_vencidos.append(prestamo_encontrado)
        self.libros.append(prestamo_encontrado.libro)

        multa = self.calcular_multa(prestamo_encontrado.fin,fecha_devolucion)
        if not multa:
            print("Libro devuelto en plazo")
        else:
            print(f"Libro devuelto fuera de plazo, por favor ingrese la multa: {multa}€")

        prestamo_encontrado.usuario.historial.append(prestamo_encontrado) #guardamos en historial
        return prestamo_encontrado
    
    def calcular_multa(self,fecha_limite,fecha_devolucion):
        """
        Calcula la cantidad de multa por devolucion tardia (10€/dia)
        devuelve None si la entrega a sido a tiempo
        """
        diferencia = fecha_devolucion - fecha_limite

        dias_retrasados = diferencia.days

        if dias_retrasados > 0:
            return dias_retrasados * self.MULTA_EUR_DIA
        return None

    def eliminar_libro(self, isbn):
        libro = self.buscar_libro(isbn)
        if not libro:
            raise RuntimeError(f"No existe ningun libro con el ISBN: {isbn}")
        self.libros.remove(libro)
        print(f"Libro eliminado satisfactoriamente -> {libro}")

    def mostrar_usuarios(self):
        print("=====USUARIOS=====")
        for usuario in self.usuarios:
            print(usuario)

    def mostrar_stock(self):
        print("=====LIBROS EN STOCK=====")
        for libro in self.libros:
            print(libro)

    def mostrar_libros_todos(self):
        print("=====TODOS LOS LIBROS=====")
        for libro in self.libros:
            print(libro)
        for prestamo in self.prestamos_activos:
            print(prestamo.libro)

    def mostrar_prestamos_activos(self):
        print("======PRÉSTAMOS ACTIVOS======")
        for item in self.prestamos_activos:
            print(item)

    def mostrar_prestamos_vencidos(self):
        print("======PRÉSTAMOS VENCIDOS======")
        for item in self.prestamos_vencidos:
            print(item)

    #funcion para importaciones (si no, no fucniona. por que havo remove(libro) cuando hago prestamos)
    def buscar_libro_total(self, isbn):

        libro = self.buscar_libro(isbn)

        if libro:
            return libro

        for prestamo in self.prestamos_activos:
            if prestamo.libro.isbn == isbn:
                return prestamo.libro

        return None