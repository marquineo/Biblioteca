from Biblioteca import Biblioteca
from Libro import Libro
from Usuario import Usuario
from datetime import datetime, date

biblioteca = Biblioteca()

print("=== Bienvenido al Sistema de Gestión de Biblioteca ===")

while True:
    print("\n¿Qué quieres hacer?")
    print("1- Registrar libro")
    print("2- Registrar usuario")
    print("3- Crear préstamo")
    print("4- Devolver libro")
    print("5- Consultar préstamos activos")
    print("6- Consultar inventario (Libros/Usuarios)")
    print("7- Salir")
    
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
                biblioteca.registrar_libro(nuevo_libro)
                print("Libro registrado con éxito.")

            case 2:
                uid = input("Dame el identificador (ID): ")
                nombre = input("Dame el nombre: ")
                nuevo_usuario = Usuario(uid, nombre)
                if biblioteca.registrar_usuario(nuevo_usuario):
                    print("Usuario registrado con éxito.")
                else:
                    print("Error: Ese identificador ya existe.")

            case 3:
                biblioteca.mostrar_info()
                isbn = input("Dime el ISBN del libro: ")
                uid = input("Dame el ID del usuario: ")
                fecha_hoy = date.today()

                prestamo = biblioteca.prestar_libro(isbn, uid, fecha_hoy)
                print(f"Préstamo creado. El libro debe devolverse el: {prestamo.fin.strftime('%d/%m/%Y')}")

            case 4:
                isbn = input("Dime el ISBN del libro a devolver: ")
                fecha_hoy = date.today()
                prestamo = biblioteca.devolver_libro(isbn, fecha_hoy)

                if prestamo:
                    print("Libro devuelto satisfactoriamente.")
                else:
                    print("No se encontró un préstamo activo para ese ISBN.")

            case 5:
                biblioteca.mostrar_prestamos_activos()

            case 6:
                biblioteca.mostrar_info()

            case 7:
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