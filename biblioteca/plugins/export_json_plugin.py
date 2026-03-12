import json

class ExportJSONPlugin:

    def exportar_libros_json(self, archivo="libros.json"):

        datos = []

        for libro in self.libros:
            datos.append({
                "isbn": libro.isbn,
                "titulo": libro.titulo,
                "autor": libro.autor
            })

        with open(archivo, "w", encoding="utf-8") as f:
            json.dump(datos, f, indent=4, ensure_ascii=False)

        print("JSON exportado correctamente")