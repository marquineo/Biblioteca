Proyecto: Sistema de gestión de biblioteca en Python
Contexto

Una biblioteca necesita un sistema software en Python para gestionar libros, usuarios y préstamos.
El objetivo de esta tarea no es hacer una aplicación completa, sino diseñar correctamente la lógica de negocio aplicando Programación Orientada a Objetos (POO).

El proyecto se desarrollará sin interfaz gráfica y sin base de datos. Todo el trabajo se realizará en memoria, priorizando el diseño, la responsabilidad de las clases y la calidad del código.
🎯 Objetivos de aprendizaje

Con esta tarea se evaluará que el alumnado sea capaz de:

    Diseñar un modelo de dominio correcto en POO.

    Distribuir responsabilidades entre clases de forma coherente.

    Aplicar encapsulación y colaboración entre objetos.

    Implementar reglas de negocio reales, no solo estructuras de datos.

    Escribir código testeable y verificable.

    Comprender que un programa puede “funcionar” y aun así estar mal diseñado.

📦 Descripción general del sistema

El sistema debe permitir:

    Registrar libros en una biblioteca.

    Registrar usuarios.

    Prestar libros a usuarios cumpliendo reglas.

    Devolver libros.

    Consultar el estado de los préstamos.

No se pide persistencia, interfaz gráfica ni menú interactivo.
🧱 Clases obligatorias

El sistema debe incluir al menos las siguientes clases:

    Libro

    Usuario

    Prestamo

    Biblioteca

    ⚠️ Importante
    Se evaluará dónde está la lógica, no solo que el sistema funcione.

📘 Clase Libro
Requisitos

    Un libro tiene:

        ISBN (único)

        título

        autor

    El libro NO debe saber si está prestado.

    El libro NO gestiona préstamos.

✔ Correcto: el libro es un objeto pasivo.
❌ Incorrecto: libro.prestado = True
👤 Clase Usuario
Requisitos

    Un usuario tiene:

        identificador

        nombre

        número máximo de préstamos simultáneos

    El usuario:

        no crea préstamos

        no almacena directamente la lista de préstamos

        no interactúa directamente con libros

🔁 Clase Prestamo (núcleo del sistema)

Esta es la clase más importante del proyecto.
Requisitos

Un préstamo:

    Relaciona un Libro y un Usuario.

    Tiene:

        fecha de inicio

        fecha límite

        fecha de devolución (opcional)

    Es responsable de:

        saber si está activo

        saber si está vencido

        calcular la multa por retraso

👉 Toda la lógica de vencimiento y multas debe estar en esta clase.
🏛️ Clase Biblioteca
Responsabilidades

La biblioteca actúa como orquestador del sistema:

    Registrar libros

    Registrar usuarios

    Crear préstamos si se cumplen las reglas

    Gestionar devoluciones

    Consultar préstamos activos

Reglas de negocio

    No se puede prestar un libro ya prestado.

    Un usuario no puede superar su límite de préstamos.

    Un préstamo no se puede devolver dos veces.

    Los errores deben gestionarse mediante excepciones explícitas.

🧪 Testing (obligatorio)

Se proporcionará una batería de tests con pytest.

    El código debe pasar los tests sin modificarlos.

    Los tests evalúan:

        diseño

        responsabilidades

        control de errores

⚠️ Manipular los tests implica calificación 0.

❌ Restricciones explícitas

No está permitido:

    Usar herencia innecesaria.

    Usar flags de estado tipo prestado = True.

    Usar fechas como strings.

    Capturar excepciones genéricas (except:).

    Devolver None silenciosamente en lugar de lanzar errores.

    Implementar lógica de préstamos en Libro o Usuario.
