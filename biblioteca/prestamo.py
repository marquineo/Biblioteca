from Libro import Libro
from Usuario import Usuario
from datetime import date, timedelta

class Prestamo:
    MULTA_DIARIA = 2

    def __init__(
        self,
        libro: Libro,
        usuario: Usuario,
        inicio: date,
        dias_maximos=10,
    ):
        self.libro = libro
        self.usuario = usuario
        self.inicio = inicio
        self.dias_maximos = dias_maximos
        self.fecha_devolucion = None
        
        # Calculamos la fecha de fin sumando los días máximos al inicio
        self.fin = inicio + timedelta(days=dias_maximos)

    def esta_activo(self) -> bool:
        """Un préstamo está activo si no ha sido devuelto aún"""
        return self.fecha_devolucion is None

    def esta_vencido(self, fecha_consulta: date = None) -> bool:
        """
        Retorna True si la fecha de consulta (o hoy) es posterior a la fecha fin
        y el libro no se ha devuelto.
        """
        if self.fecha_devolucion is not None:
            return False
        
        # Si el test no pasa fecha, usamos hoy
        comparar_con = fecha_consulta if fecha_consulta else date.today()
        return comparar_con > self.fin

    def calcular_multa(self, fecha_consulta: date = None) -> int:
        """Calcula la multa comparando la fecha de devolución (o consulta) con el fin"""
        # Determinamos qué fecha usar para el cálculo
        fecha_final = self.fecha_devolucion if self.fecha_devolucion else fecha_consulta
        
        if not fecha_final or fecha_final <= self.fin:
            return 0
            
        dias_retraso = (fecha_final - self.fin).days
        return dias_retraso * self.MULTA_DIARIA

    def devolver(self, fecha: date):
        """Registra la devolución. Lanza RuntimeError si ya estaba devuelto"""
        if self.fecha_devolucion is not None:
            raise RuntimeError("El libro ya ha sido devuelto anteriormente")
        
        if fecha < self.inicio:
            raise ValueError("La devolución no puede ser antes del inicio")
            
        self.fecha_devolucion = fecha

    def __str__(self):
        # Mantenemos tu str pero ajustando nombres de variables
        estado = "Devuelto" if self.fecha_devolucion else ("Vencido" if self.esta_vencido() else "Activo")
        fecha_dev = self.fecha_devolucion.strftime("%d/%m/%Y") if self.fecha_devolucion else "—"
        
        return (
            f"Préstamo:\n"
            f"  Libro: {self.libro.titulo}\n"
            f"  Usuario: {self.usuario.nombre}\n"
            f"  Fin: {self.fin.strftime('%d/%m/%Y')}\n"
            f"  Estado: {estado}"
        )