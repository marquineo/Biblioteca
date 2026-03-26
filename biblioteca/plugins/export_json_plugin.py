import json

class ExportJSONPlugin:

    def exportar_libros_json(self, archivo="libros.json"):

        datos = []
        libros_exportados = {}

        # libros disponibles
        for libro in self.libros:
            libros_exportados[libro.isbn] = libro

        # libros en préstamos activos
        for prestamo in self.prestamos_activos:
            libros_exportados[prestamo.libro.isbn] = prestamo.libro

        # libros en préstamos vencidos
        for prestamo in self.prestamos_vencidos:
            libros_exportados[prestamo.libro.isbn] = prestamo.libro

        for libro in libros_exportados.values():
            datos.append({
                "isbn": libro.isbn,
                "titulo": libro.titulo,
                "autor": libro.autor
            })

        with open(archivo, "w", encoding="utf-8") as f:
            json.dump(datos, f, indent=4, ensure_ascii=False)

        print("JSON exportado correctamente")