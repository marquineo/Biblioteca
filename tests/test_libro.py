import pytest
from biblioteca.Libro import Libro


def test_creacion_libro_basica():
    libro = Libro("123", "Titulo", "Autor")
    assert libro.isbn == "123"
    assert libro.titulo == "Titulo"
    assert libro.autor == "Autor"


def test_isbn_obligatorio():
    with pytest.raises(ValueError):
        Libro("", "Titulo", "Autor")


def test_libro_no_tiene_estado_prestamo():
    libro = Libro("123", "Titulo", "Autor")
    assert not hasattr(libro, "prestado")
    assert not hasattr(libro, "esta_prestado")
