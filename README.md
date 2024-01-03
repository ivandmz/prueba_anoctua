PROCEDIMIENTO

1- Se clona el repo, se crea repo local y nuevo repo. Se cambia remote por el del nuevo repo, actualizando .gitignore para basico de python.
2- Se crea ambiente virtual, se activa e instalan paquetes (django, DRF, pandas, sqlalchemy, etc).
3- Creación de listado de requirements (ver detalle debajo).
4- Para el primer punto se crea el script en etls/main.py utilizando pandas para cargar el archivo y generar la tabla y sqlalchemy para vincularlo a la DB.
5- Al correr el archivo se genera en la base de datos la tabla "cotizaciones" requerida.
6- Para el segundo item se generó una app llamada 'api' con el model 'Cotizacion', su serializer y su viewset
7- Se incluyó routers en urls.py
8- Se realizan migraciones (makemigrations & migrate)
9- Testeo del endpoint generado. Por ejemplo: http://localhost:8000/cotizaciones/promediar_periodo/?fecha_inicio=2018-07-04&fecha_fin=2018-07-17          con resultado positivo.



-------------------------------------------------
REFERENCIAS
https://www.djangoproject.com/
https://docs.djangoproject.com/es/5.0/topics/db/aggregation/
https://www.django-rest-framework.org/
https://medium.com/@nicolasurrego/c%C3%B3mo-cargar-un-archivo-csv-en-python-considerando-sus-caracter%C3%ADsticas-5cb0ca74e9d
https://www.analyticslane.com/2019/05/06/como-cambiar-el-nombre-de-las-columnas-en-pandas/
https://j2logo.com/python/sqlalchemy-tutorial-de-python-sqlalchemy-guia-de-inicio/


-------------------------------------------------
*REQUIREMENTS.TXT*

asgiref==3.7.2
backports.zoneinfo==0.2.1
Django==4.2.9
djangorestframework==3.14.0
greenlet==3.0.3
numpy==1.24.4
pandas==2.0.3
python-dateutil==2.8.2
pytz==2023.3.post1
six==1.16.0
SQLAlchemy==2.0.24
sqlparse==0.4.4
typing-extensions==4.9.0
tzdata==2023.4
