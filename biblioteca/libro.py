class Libro:
    def __init__(self, isbn, titulo, autor):
        if isbn == "":
            raise ValueError("el ISBN no puede estar vacio")
        self.isbn = isbn
        self.titulo = titulo
        self.autor = autor

    def __str__(self):
        return f"ISBN: {self.isbn} | Autor: {self.autor} | Título: {self.titulo}"
