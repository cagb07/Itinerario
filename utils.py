"""
Módulo de utilidades compartidas entre módulos de la aplicación
"""
import pandas as pd

def guardar_seguimiento(df, archivo_seguimiento):
    """Guarda el DataFrame de seguimiento en el archivo CSV"""
    df.to_csv(archivo_seguimiento, index=False)
