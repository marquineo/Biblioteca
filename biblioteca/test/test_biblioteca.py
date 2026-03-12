import unittest
from datetime import date

from biblioteca import Biblioteca
from libro import Libro
from usuario import Usuario


class TestBiblioteca(unittest.TestCase):

    def setUp(self):
        self.b = Biblioteca()

    def test_registrar_usuario(self):
        u = Usuario("U100", "Test")

        resultado = self.b.registrar_usuario(u)

        self.assertTrue(resultado)
        self.assertIsNotNone(self.b.buscar_usuario("U100"))

    def test_usuario_duplicado(self):
        u = Usuario("U200", "Test")

        self.b.registrar_usuario(u)
        resultado = self.b.registrar_usuario(u)

        self.assertFalse(resultado)

    def test_registrar_libro(self):
        l = Libro("999", "Test Libro", "Autor")

        self.b.registrar_libro(l)

        encontrado = self.b.buscar_libro("999")

        self.assertEqual(encontrado, l)

    def test_prestar_libro(self):
        libro = self.b.libros[0]
        usuario = self.b.usuarios[0]

        prestamo = self.b.prestar_libro(libro.isbn, usuario.id, date.today())

        self.assertIsNotNone(prestamo)
        self.assertEqual(len(self.b.prestamos_activos), 1)

    def test_devolver_libro(self):
        libro = self.b.libros[0]
        usuario = self.b.usuarios[0]

        self.b.prestar_libro(libro.isbn, usuario.id, date.today())

        devuelto = self.b.devolver_libro(libro.isbn, date.today())

        self.assertIsNotNone(devuelto)
        self.assertEqual(len(self.b.prestamos_activos), 0)


if __name__ == "__main__":
    unittest.main()