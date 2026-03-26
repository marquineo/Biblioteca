from biblioteca import Biblioteca
from libro import Libro
from usuario import Usuario
from datetime import date,timedelta
from data_io_mixin import DataIOMixin

from plugin_loader import cargar_plugins


# ===============================
# CARGA DINÁMICA DE PLUGINS
# ===============================

plugins = cargar_plugins()

BibliotecaFinal = type(
    "BibliotecaFinal",
    tuple([DataIOMixin, Biblioteca] + plugins),
    {}
)

biblioteca = BibliotecaFinal()

#Muestra plugins cargados
print("Plugins cargados:")
for p in plugins:
    print("-", p.__name__)

# ===============================
# PROGRAMA PRINCIPAL
# ===============================

print("=== Bienvenido al Sistema de Gestión de Biblioteca ===")

while True:
    print("\n¿Qué quieres hacer?")
    print("1- Registrar libro")
    print("2- Registrar usuario")
    print("3- Eliminar libro")
    print("4- Crear préstamo")
    print("5- Devolver libro")
    print("6- Consultar préstamos activos")
    print("7- Consultar préstamos vencidos")
    print("8- Consultar inventario y exportaciones")
    print("9- Listar usuarios")
    print("10- Salir")

    opcion = input("Selecciona una opción: ")

    if not opcion.isdigit():
        print("Error: La opción debe ser un número.")
        continue
    opcion = int(opcion)

    try:
        match opcion:

            case 1:
                isbn = input("Dame el ISBN: ")
                titulo = input("Dame el título: ")
                autor = input("Dame el autor: ")

                nuevo_libro = Libro(isbn, titulo, autor)

                biblioteca = biblioteca + nuevo_libro

                print("Libro registrado con éxito.")

            case 2:

                uid = input("Dame el identificador (ID): ")
                nombre = input("Dame el nombre: ")
                max_prestamos = input("Cuantos prestamos puede tener a la vez?")

                if max_prestamos == "":
                    nuevo_usuario = Usuario(uid, nombre)
                else:
                    if not max_prestamos.isdigit():
                        print("Introduce un número")
                        continue

                    max_prestamos = int(max_prestamos)
                    nuevo_usuario = Usuario(uid, nombre, max_prestamos)

                if biblioteca.registrar_usuario(nuevo_usuario):
                    print("Usuario registrado con éxito.")
                else:
                    print("Error: Ese identificador ya existe.")

            case 3:
                isbn_del = input("Dame el ISBN del libro que quieres eliminar: ")
                biblioteca.eliminar_libro(isbn_del)

            case 4:

                biblioteca.mostrar_stock()
                biblioteca.mostrar_usuarios()

                isbn = input("Dime el ISBN del libro: ")
                uid = input("Dame el ID del usuario: ")

                fecha_hoy = date.today()

                prestamo = biblioteca.prestar_libro(isbn, uid, fecha_hoy)

                print(
                    f"Préstamo creado. El libro debe devolverse el: {prestamo.fin.strftime('%d/%m/%Y')}"
                )

            case 5:

                isbn = input("Dime el ISBN del libro a devolver: ")

                fecha_hoy = date.today()
                fecha_en_10_dias = fecha_hoy + timedelta(days=20) #Debug multa

                prestamo = biblioteca.devolver_libro(isbn, fecha_hoy)

                if prestamo:
                    print("Libro devuelto satisfactoriamente.")
                else:
                    print("No se encontró un préstamo activo para ese ISBN.")

            case 6:

                biblioteca.mostrar_prestamos_activos()

            case 7:

                biblioteca.mostrar_prestamos_vencidos()

            case 8:

                while True:

                    print("\n¿Qué quieres hacer?")
                    print("1- Mostrar libros en stock")
                    print("2- mostrar todos los libros")
                    print("3- Mostrar usuarios")
                    print("4- Exportar datos CSV")
                    print("5- Exportar datos JSON")
                    print("6- Importar datos CSV")
                    print("7- Importar datos JSON")
                    print("8- Salir")

                    entrada = input("Selecciona una opción: ")

                    if not entrada.isdigit():
                        print("Introduzca un número")
                        continue

                    entrada = int(entrada)

                    match entrada:

                        case 1:
                            biblioteca.mostrar_stock()

                        case 2:
                            biblioteca.mostrar_libros_todos()

                        case 3:
                            biblioteca.mostrar_usuarios()

                        case 4:
                            biblioteca.exportar_libros_csv()
                            biblioteca.exportar_usuarios_csv()
                            biblioteca.exportar_prestamos_csv()
                        case 5:
                            biblioteca.exportar_libros_json()
                            biblioteca.exportar_usuarios_json()
                            biblioteca.exportar_prestamos_json()
                        case 6:
                            biblioteca.importar_libros_csv()
                            biblioteca.importar_usuarios_csv()
                            biblioteca.importar_prestamos_csv()
                        case 7:
                            biblioteca.importar_libros_json()
                            biblioteca.importar_usuarios_json()
                            biblioteca.importar_prestamos_json()
                        case 8:
                            print("Volviendo al menú principal....")
                            break

                        case _:
                            print("Opción no válida (1-4).")

            case 9:
                print("***USUARIOS***")
                biblioteca.mostrar_usuarios()
            case 10:

                print("Saliendo del sistema...")
                break

            case _:
                print("Opción no válida (1-7).")

    except RuntimeError as e:
        print(f"Error de operación: {e}")

    except ValueError as e:
        print(f"Error de datos: {e}")

    except Exception as e:
        print(f"Ha ocurrido un error inesperado: {e}")
