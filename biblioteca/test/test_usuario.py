import unittest
from usuario import Usuario


class TestUsuario(unittest.TestCase):

    def test_creacion_usuario(self):
        u = Usuario("U1", "Ana")
        self.assertEqual(u.id, "U1")
        self.assertEqual(u.nombre, "Ana")
        self.assertEqual(u.max_prestamos, 3)

    def test_max_prestamos_invalido(self):
        with self.assertRaises(ValueError):
            Usuario("U1", "Ana", 0)

    def test_call_devuelve_id(self):
        u = Usuario("U1", "Ana")
        self.assertEqual(u(), "U1")


if __name__ == "__main__":
    unittest.main()