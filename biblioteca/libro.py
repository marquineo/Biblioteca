class Libro:
    def __init__(self, isbn, titulo, autor):
        self.isbn = isbn
        self.titulo = titulo
        self.autor = autor

    def __str__(self):
        return f"ISBN: {self.isbn} | Autor: {self.autor} | Título: {self.titulo}"
