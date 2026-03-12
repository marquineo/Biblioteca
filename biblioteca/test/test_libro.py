import unittest
from libro import Libro


class TestLibro(unittest.TestCase):

    def test_creacion_libro(self):
        libro = Libro("123", "Python", "Guido")
        self.assertEqual(libro.isbn, "123")
        self.assertEqual(libro.titulo, "Python")
        self.assertEqual(libro.autor, "Guido")

    def test_isbn_vacio(self):
        with self.assertRaises(ValueError):
            Libro("", "Titulo", "Autor")

    def test_igualdad_libros(self):
        l1 = Libro("111", "A", "Autor")
        l2 = Libro("111", "B", "Autor2")
        self.assertEqual(l1, l2)

    def test_repr(self):
        libro = Libro("123", "Python", "Guido")
        self.assertIn("ISBN", repr(libro))


if __name__ == "__main__":
    unittest.main()