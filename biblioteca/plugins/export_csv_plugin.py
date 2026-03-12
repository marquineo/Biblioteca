import csv

class ExportCSVPlugin:

    def exportar_libros_csv(self, archivo="libros.csv"):

        with open(archivo, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)

            writer.writerow(["ISBN", "Titulo", "Autor"])

            for libro in self.libros:
                writer.writerow([libro.isbn, libro.titulo, libro.autor])

        print("CSV exportado correctamente")