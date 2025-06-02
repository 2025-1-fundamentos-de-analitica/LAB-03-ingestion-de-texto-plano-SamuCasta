"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta.
"""

# pylint: disable=import-outside-toplevel


def pregunta_01():
    """
    Construya y retorne un dataframe de Pandas a partir del archivo
    'files/input/clusters_report.txt'. Los requierimientos son los siguientes:

    - El dataframe tiene la misma estructura que el archivo original.
    - Los nombres de las columnas deben ser en minusculas, reemplazando los
      espacios por guiones bajos.
    - Las palabras clave deben estar separadas por coma y con un solo
      espacio entre palabra y palabra.
    """
    
    import pandas as pd

    # Lista para guardar bloques de texto que corresponden a cada fila de la tabla
    bloques_de_fila = []
    bloque_actual = []

    # Abrir el archivo de texto plano
    with open("files/input/clusters_report.txt") as archivo:
        lineas_crudas = archivo.readlines()

    # Saltar las primeras 4 líneas (encabezado no tabular)
    for linea in lineas_crudas[4:]:
        if linea.strip():  # Línea con contenido
            bloque_actual.append(linea.strip())
        else:  # Línea vacía indica fin de un bloque (una fila completa)
            if bloque_actual:
                bloques_de_fila.append(" ".join(bloque_actual))  # Unir y guardar el bloque
                bloque_actual = []

    datos_procesados = []

    # Procesar cada fila combinada
    for fila in bloques_de_fila:
        partes = fila.split()
        cluster_id = int(partes[0])  # Primer valor: ID del cluster
        cantidad_palabras = int(partes[1])  # Segundo valor: cantidad de palabras clave
        porcentaje_palabras = float(partes[2].replace(",", "."))  # Tercer valor: porcentaje
        palabras_clave = (
            " ".join(partes[3:])  # Unir el resto como texto
            .replace(" ,", ",")   # Limpiar coma mal separada
            .strip("%")           # Quitar símbolo de porcentaje si queda
            .rstrip(".")          # Quitar punto final
            .strip()              # Quitar espacios en los extremos
        )
        datos_procesados.append([cluster_id, cantidad_palabras, porcentaje_palabras, palabras_clave])

    # Nombres limpios de columnas para el DataFrame final
    nombres_columnas = [
        "cluster",
        "cantidad_de_palabras_clave",
        "porcentaje_de_palabras_clave",
        "principales_palabras_clave"
    ]

    # Crear DataFrame con los datos organizados
    df_clusters = pd.DataFrame(datos_procesados, columns=nombres_columnas)

    import os
    os.makedirs("files/output", exist_ok=True)
    df_clusters.to_csv("files/output/clusters_report.csv", index=False, encoding="utf-8")

    # Devolver el DataFrame 
    return (df_clusters)
