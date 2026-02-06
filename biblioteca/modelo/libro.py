class Libro:
    def __init__(self, isbn, titulo, autor):
        if isbn == "":
            raise ValueError("el ISBN no puede estar vacio")
        self.isbn = isbn
        self.titulo = titulo
        self.autor = autor

    def __str__(self):
        return f"ISBN: {self.isbn} | Autor: {self.autor} | Título: {self.titulo}"
    
    def __repr__(self):
        return f"ISBN = {self.isbn} --- Autor = {self.autor} --- Título = {self.titulo}"
    
    def __eq__(self, other):
        if not isinstance(other, Libro):
            return NotImplemented
        return self.isbn == other.isbn

    def __hash__(self):
        return hash(self.titulo,self.autor,self.isbn)