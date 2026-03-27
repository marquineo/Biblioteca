class Libro:
    def __init__(self, isbn, titulo, autor):
        """
        Constructor de la clase Libro.

        Parámetros:
        - isbn: identificador único del libro
        - titulo: título del libro
        - autor: autor del libro
        """

        # Validación: el ISBN no puede estar vacío
        if isbn == "":
            raise ValueError("el ISBN no puede estar vacio")

        self.isbn = isbn
        self.titulo = titulo
        self.autor = autor

    def __str__(self):
        """
        Representación en texto legible para el usuario.
        Se utiliza al hacer print(libro).
        """
        return f"ISBN: {self.isbn} | Autor: {self.autor} | Título: {self.titulo}"
    
    def __repr__(self):
        """
        Representación más detallada, útil para depuración.
        Se utiliza cuando se imprime el objeto en listas o consola.
        """
        return f"ISBN = {self.isbn} --- Autor = {self.autor} --- Título = {self.titulo}"
    
    def __eq__(self, other):
        """
        Define cuándo dos libros son iguales.

        Dos libros se consideran iguales si tienen el mismo ISBN,
        independientemente del resto de atributos.
        """
        if not isinstance(other, Libro):
            return NotImplemented
        return self.isbn == other.isbn

    def __hash__(self):
        """
        Permite usar objetos Libro en estructuras como sets o diccionarios.

        IMPORTANTE:
        Debe ser coherente con __eq__, por lo que se basa en el ISBN.
        """
        return hash(self.isbn)