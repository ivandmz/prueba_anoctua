## escriba el pipeline aqui

import pandas as pd
from sqlalchemy import create_engine


# Ruta del archivo
archivo_csv = './data/data.csv'

# Create your views here.
def script_ETL():
    # Cargar el archivo CSV en un DataFrame
    df = pd.read_csv(archivo_csv, header=0,delimiter=',')
    #  Nombrar columnas
    df.columns = ['fecha','tipo_de_cambio']

    # Conexion a DB usando sqlalchemy
    engine = create_engine("sqlite:///prueba_anoctua.sqlite")

    # Cargar datos en la tabla "cotizaciones"
    df.to_sql('cotizaciones', engine, if_exists='replace', index=False)
    
    # Mensaje de confirmacion
    print("Datos cargados exitosamente en la tabla.")



if __name__ == "__main__":
    script_ETL()