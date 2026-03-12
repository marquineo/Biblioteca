import os
import importlib
import inspect


def cargar_plugins():

    plugins = []

    # ruta absoluta de la carpeta actual
    base_dir = os.path.dirname(__file__)

    # ruta absoluta a plugins
    carpeta_plugins = os.path.join(base_dir, "plugins")

    for archivo in os.listdir(carpeta_plugins):

        if archivo.endswith(".py") and archivo != "__init__.py":

            nombre_modulo = archivo[:-3]#quita el '.py'

            modulo = importlib.import_module(f"plugins.{nombre_modulo}")

            for nombre, objeto in inspect.getmembers(modulo, inspect.isclass): #Busca que sean clases (.isclass)

                if nombre.endswith("Plugin"):#si la clase termina en "Plugin" lo guarda en la lista plugins
                    plugins.append(objeto)

    return plugins