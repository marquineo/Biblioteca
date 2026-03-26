import csv
import json
from datetime import date
from libro import Libro
from usuario import Usuario
from prestamo import Prestamo


class DataIOMixin:

    # ======================
    # LIBROS
    # ======================

    def importar_libros_csv(self, archivo="libros.csv"):

        with open(archivo, newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)

            contador = 0

            for fila in reader:

                isbn = fila["ISBN"]
                titulo = fila["Titulo"]
                autor = fila["Autor"]

                if not self.buscar_libro(isbn):

                    libro = Libro(isbn, titulo, autor)
                    self.registrar_libro(libro)

                    contador += 1

        print(f"{contador} libros importados desde CSV")

    # def exportar_libros_csv(self, archivo="libros.csv"):

    #     with open(archivo, "w", newline="", encoding="utf-8") as f:

    #         writer = csv.writer(f)
    #         writer.writerow(["ISBN", "Titulo", "Autor"])

    #         for libro in self.libros:
    #             writer.writerow([libro.isbn, libro.titulo, libro.autor])

    #     print("Libros exportados correctamente a CSV")

    def importar_libros_json(self, archivo="libros.json"):

        with open(archivo, encoding="utf-8") as f:
            datos = json.load(f)

        contador = 0

        for item in datos:

            if not self.buscar_libro(item["isbn"]):

                libro = Libro(item["isbn"], item["titulo"], item["autor"])
                self.registrar_libro(libro)

                contador += 1

        print(f"{contador} libros importados desde JSON")

    # def exportar_libros_json(self, archivo="libros.json"):

    #     datos = []

    #     for libro in self.libros:

    #         datos.append({
    #             "isbn": libro.isbn,
    #             "titulo": libro.titulo,
    #             "autor": libro.autor
    #         })

    #     with open(archivo, "w", encoding="utf-8") as f:
    #         json.dump(datos, f, indent=4, ensure_ascii=False)

    #     print("Libros exportados a JSON")

    # ======================
    # USUARIOS
    # ======================

    def exportar_usuarios_csv(self, archivo="usuarios.csv"):

        with open(archivo, "w", newline="", encoding="utf-8") as f:

            writer = csv.writer(f)
            writer.writerow(["ID", "Nombre", "MaxPrestamos"])

            for usuario in self.usuarios:
                writer.writerow([usuario.id, usuario.nombre, usuario.max_prestamos])

        print("Usuarios exportados a CSV")

    def importar_usuarios_csv(self, archivo="usuarios.csv"):

        with open(archivo, newline="", encoding="utf-8") as f:

            reader = csv.DictReader(f)

            contador = 0

            for fila in reader:

                if not self.buscar_usuario(fila["ID"]):

                    usuario = Usuario(
                        fila["ID"], fila["Nombre"], int(fila["MaxPrestamos"])
                    )

                    self.registrar_usuario(usuario)

                    contador += 1

        print(f"{contador} usuarios importados desde CSV")

    def exportar_usuarios_json(self, archivo="usuarios.json"):

        datos = []

        for usuario in self.usuarios:

            datos.append(
                {
                    "id": usuario.id,
                    "nombre": usuario.nombre,
                    "max_prestamos": usuario.max_prestamos,
                }
            )

        with open(archivo, "w", encoding="utf-8") as f:
            json.dump(datos, f, indent=4, ensure_ascii=False)

        print("Usuarios exportados a JSON")

    def importar_usuarios_json(self, archivo="usuarios.json"):

        with open(archivo, encoding="utf-8") as f:
            datos = json.load(f)

        contador = 0

        for item in datos:

            if not self.buscar_usuario(item["id"]):

                usuario = Usuario(item["id"], item["nombre"], item["max_prestamos"])

                self.registrar_usuario(usuario)

                contador += 1

        print(f"{contador} usuarios importados desde JSON")

    # ======================
    # PRÉSTAMOS
    # ======================

    def exportar_prestamos_json(self, archivo="prestamos.json"):

        datos = []

        for prestamo in self.prestamos_activos:

            datos.append(
                {
                    "isbn": prestamo.libro.isbn,
                    "usuario": prestamo.usuario.id,
                    "inicio": prestamo.inicio.isoformat(),
                    "fin": prestamo.fin.isoformat(),
                }
            )

        with open(archivo, "w", encoding="utf-8") as f:
            json.dump(datos, f, indent=4)

        print("Préstamos exportados a JSON")

    def importar_prestamos_json(self, archivo="prestamos.json"):

        with open(archivo, encoding="utf-8") as f:
            datos = json.load(f)

        contador = 0

        for item in datos:

            libro = self.buscar_libro_total(item["isbn"])
            usuario = self.buscar_usuario(item["usuario"])

            if libro and usuario:

                inicio = date.fromisoformat(item["inicio"])
                fin = date.fromisoformat(item["fin"])

                dias = (fin - inicio).days

                prestamo = Prestamo(libro, usuario, inicio, dias)

                self.prestamos_activos.append(prestamo)

                if libro in self.libros:
                    self.libros.remove(libro)

                contador += 1

        print(f"{contador} préstamos importados desde JSON")

    def exportar_prestamos_csv(self, archivo="prestamos.csv"):

        with open(archivo, "w", newline="", encoding="utf-8") as f:

            writer = csv.writer(f)

            writer.writerow(
                ["ISBN", "UsuarioID", "FechaInicio", "FechaFin", "FechaDevolucion"]
            )

            for prestamo in self.prestamos_activos:

                writer.writerow(
                    [
                        prestamo.libro.isbn,
                        prestamo.usuario.id,
                        prestamo.inicio.isoformat(),
                        prestamo.fin.isoformat(),
                        (
                            prestamo.fecha_devolucion.isoformat()
                            if prestamo.fecha_devolucion
                            else ""
                        ),
                    ]
                )

        print("Préstamos exportados correctamente a CSV")

    def importar_prestamos_csv(self, archivo="prestamos.csv"):

        with open(archivo, newline="", encoding="utf-8") as f:

            reader = csv.DictReader(f)

            contador = 0

            for fila in reader:

                libro = self.buscar_libro_total(fila["ISBN"])
                usuario = self.buscar_usuario(fila["UsuarioID"])

                if libro and usuario:

                    inicio = date.fromisoformat(fila["FechaInicio"])
                    fin = date.fromisoformat(fila["FechaFin"])

                    dias = (fin - inicio).days

                    prestamo = Prestamo(libro, usuario, inicio, dias)

                    if fila["FechaDevolucion"]:
                        prestamo.fecha_devolucion = date.fromisoformat(
                            fila["FechaDevolucion"]
                        )

                    self.prestamos_activos.append(prestamo)

                    if libro in self.libros:
                        self.libros.remove(libro)

                    contador += 1

        print(f"{contador} préstamos importados desde CSV")
