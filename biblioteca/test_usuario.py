import pytest
from Usuario import Usuario


def test_usuario_basico():
    usuario = Usuario(1, "Ana", max_prestamos=2)
    assert usuario.id == 1
    assert usuario.nombre == "Ana"
    assert usuario.max_prestamos == 2


def test_limite_prestamos_positivo():
    with pytest.raises(ValueError):
        Usuario(1, "Ana", max_prestamos=0)


def test_usuario_no_gestiona_prestamos():
    usuario = Usuario(1, "Ana")
    assert not hasattr(usuario, "prestamos")
    assert not hasattr(usuario, "prestar")
