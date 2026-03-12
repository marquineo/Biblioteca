class EstadisticasPlugin:

    def total_libros(self):
        return len(self.libros)

    def total_usuarios(self):
        return len(self.usuarios)

    def libro_mas_prestado(self):

        contador = {}

        for prestamo in self.prestamos_activos + self.prestamos_vencidos:
            titulo = prestamo.libro.titulo
            contador[titulo] = contador.get(titulo, 0) + 1

        if not contador:
            return None

        return max(contador, key=contador.get)