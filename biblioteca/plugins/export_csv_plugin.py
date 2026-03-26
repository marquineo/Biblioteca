import csv

class ExportCSVPlugin:

    def exportar_libros_csv(self, archivo="libros.csv"):

        with open(archivo, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)

            writer.writerow(["ISBN", "Titulo", "Autor"])

            libros_exportados = {}

            # disponibles
            for libro in self.libros:
                libros_exportados[libro.isbn] = libro

            # prestados activos
            for prestamo in self.prestamos_activos:
                libros_exportados[prestamo.libro.isbn] = prestamo.libro

            # vencidos
            for prestamo in self.prestamos_vencidos:
                libros_exportados[prestamo.libro.isbn] = prestamo.libro

            for libro in libros_exportados.values():
                writer.writerow([libro.isbn, libro.titulo, libro.autor])

        print("CSV exportado correctamente")