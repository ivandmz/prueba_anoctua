from django.shortcuts import render
import pandas as pd
from sqlalchemy import create_engine
from settings import DATABASES


# Ruta del archivo
archivo_csv = '../data/data.csv'

# Create your views here.
def script_ETL():
    # Cargar el archivo CSV en un DataFrame
    df = pd.read_csv(archivo_csv, header=0)
    #  Nombrar columnas
    df.columns = ['fecha','tipo_de_cambio.']

    #conexion a DB usando sqlalchemy
    engine = create_engine(DATABASES)