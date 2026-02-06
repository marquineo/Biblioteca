from datetime import date, timedelta
import pytest
from libro import Libro
from usuario import Usuario
from prestamo import Prestamo


def crear_prestamo_activo():
    libro = Libro("123", "Python", "Autor")
    usuario = Usuario(1, "Ana")
    return Prestamo(libro, usuario, date(2025, 1, 1), dias_maximos=7)


def test_prestamo_activo_por_defecto():
    prestamo = crear_prestamo_activo()
    assert prestamo.esta_activo() is True


def test_prestamo_no_vencido_inicialmente():
    prestamo = crear_prestamo_activo()
    assert prestamo.esta_vencido(date(2025, 1, 5)) is False


def test_prestamo_vencido():
    prestamo = crear_prestamo_activo()
    assert prestamo.esta_vencido(date(2025, 1, 10)) is True


def test_devolucion_cierra_prestamo():
    prestamo = crear_prestamo_activo()
    prestamo.devolver(date(2025, 1, 5))
    assert prestamo.esta_activo() is False


def test_no_se_puede_devolver_dos_veces():
    prestamo = crear_prestamo_activo()
    prestamo.devolver(date(2025, 1, 5))
    with pytest.raises(RuntimeError):
        prestamo.devolver(date(2025, 1, 6))


def test_calculo_multa():
    prestamo = crear_prestamo_activo()
    fecha = date(2025, 1, 10)  # 2 días de retraso
    assert prestamo.calcular_multa(fecha) == 2 * Prestamo.MULTA_DIARIA
