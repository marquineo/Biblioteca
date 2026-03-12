import unittest
from datetime import date, timedelta

from libro import Libro
from usuario import Usuario
from prestamo import Prestamo


class TestPrestamo(unittest.TestCase):

    def setUp(self):
        self.libro = Libro("111", "Libro Test", "Autor")
        self.usuario = Usuario("U1", "Ana")
        self.fecha = date.today()

    def test_creacion_prestamo(self):
        p = Prestamo(self.libro, self.usuario, self.fecha)

        self.assertEqual(p.libro, self.libro)
        self.assertEqual(p.usuario, self.usuario)
        self.assertTrue(p.esta_activo())

    def test_prestamo_vencido(self):
        p = Prestamo(self.libro, self.usuario, self.fecha - timedelta(days=20))
        self.assertTrue(p.esta_vencido())

    def test_devolver_libro(self):
        p = Prestamo(self.libro, self.usuario, self.fecha)
        p.devolver(self.fecha + timedelta(days=2))

        self.assertFalse(p.esta_activo())

    def test_calculo_multa(self):
        p = Prestamo(self.libro, self.usuario, self.fecha - timedelta(days=20))
        multa = p.calcular_multa(date.today())

        self.assertGreater(multa, 0)


if __name__ == "__main__":
    unittest.main()