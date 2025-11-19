import os
import json

# Nombre del archivo JSON
nombre_archivo = "datos.json"

# Verificar si el archivo .json existe en el directorio actual
if os.path.exists(nombre_archivo):
    print(f"El archivo '{nombre_archivo}' ya existe. Abriéndolo...")
    # Abrir y leer el contenido del archivo
    with open(nombre_archivo, 'r+', encoding='utf-8') as archivo:
        try:
            datos = json.load(archivo)
        except json.JSONDecodeError:
            print("El archivo existe pero está vacío o corrupto. Reiniciando con un JSON vacío.")
            datos = {}
            archivo.seek(0)
            json.dump(datos, archivo, indent=4)
            archivo.truncate()
else:
    print(f"El archivo '{nombre_archivo}' no existe. Creándolo vacío...")
    # Crear el archivo con un JSON vacío
    with open(nombre_archivo, 'w', encoding='utf-8') as archivo:
        json.dump({}, archivo, indent=4)
    # Reabrirlo para lectura/escritura
    with open(nombre_archivo, 'r+', encoding='utf-8') as archivo:
        datos = {}

print(f"Archivo '{nombre_archivo}' abierto correctamente.")
print("Contenido actual del archivo:")
print(json.dumps(datos, indent=4, ensure_ascii=False))
