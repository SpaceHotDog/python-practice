# Importamos dependencias.
from sqlalchemy import *

# Creamos una variable #engine, que contiene el metodo de conexion del objeto Engine.
#Mas info en docs.sqlalchemy.org/en/latest/core/engines.html
engine = create_engine('lenguaje+driver://usuario:contraseña@host:puerto/nombreDB')

#Definimos la variable que contiene el metodo de conexion.
connection = engine.connect()

# Usamos el método table_names sobre el engine para obtener los nombres de las tablas, y luego las guardamos en la variable 'var'.
var = print(engine.table_names())

#Inicializamos la variable #meta donde se guarda la metadata.
meta = MetaData()

#Guardamos los nombres de las columnas en la variable #messages.
messages = Table('messages', meta, autoload=True, autoload_with=engine)
