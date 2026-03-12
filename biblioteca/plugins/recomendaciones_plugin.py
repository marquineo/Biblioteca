class RecomendacionesPlugin:

    def recomendar_por_autor(self, autor):

        resultado = []

        for libro in self.libros:
            if libro.autor.lower() == autor.lower():
                resultado.append(libro)

        return resultado