from datetime import date
import pytest
from biblioteca import Biblioteca
from libro import Libro
from usuario import Usuario


@pytest.fixture
def biblioteca_basica():
    b = Biblioteca()
    b.registrar_libro(Libro("123", "Python", "Autor"))
    b.registrar_usuario(Usuario(1, "Ana", max_prestamos=1))
    return b


def test_prestar_libro_correcto(biblioteca_basica):
    prestamo = biblioteca_basica.prestar_libro(
        "123", 1, date(2025, 1, 1)
    )
    assert prestamo.esta_activo()


def test_no_prestar_libro_ya_prestado(biblioteca_basica):
    biblioteca_basica.prestar_libro("123", 1, date(2025, 1, 1))
    with pytest.raises(RuntimeError):
        biblioteca_basica.prestar_libro("123", 1, date(2025, 1, 2))


def test_usuario_supera_limite(biblioteca_basica):
    biblioteca_basica.prestar_libro("123", 1, date(2025, 1, 1))

    libro2 = Libro("456", "Otro", "Autor")
    biblioteca_basica.registrar_libro(libro2)

    with pytest.raises(RuntimeError):
        biblioteca_basica.prestar_libro("456", 1, date(2025, 1, 2))


def test_devolver_libro(biblioteca_basica):
    biblioteca_basica.prestar_libro("123", 1, date(2025, 1, 1))
    prestamo = biblioteca_basica.devolver_libro(
        "123", date(2025, 1, 5)
    )
    assert prestamo.esta_activo() is False
