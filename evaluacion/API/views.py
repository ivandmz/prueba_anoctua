from django.shortcuts import render
import pandas as pd
from sqlalchemy import create_engine


# Ruta del archivo
archivo_csv = '../data/data.csv'

# Create your views here.
def script_ETL():
    # Cargar el archivo CSV en un DataFrame
    df = pd.read_csv(archivo_csv, header=0)
    df.columns = ['fecha','tipo_de_cambio.']