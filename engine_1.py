# Importamos dependencias.
from sqlalchemy import create_engine

# Creamos un engine apuntando a la base de datos elegida. En este caso, 'census'. 
# El ejemplo utiliza una DB PostgreSQL alojada en AWS.
#Mas info en http://docs.sqlalchemy.org/en/latest/core/engines.html
engine = create_engine('postgresql+psycopg2://student:datacamp@postgresql.csrrinzqubik.us-east-1.rds.amazonaws.com:5432/census')

#Nos conectamos a la base de datos.
connection = engine.connect()

# Usamos el método table_names sobre el engine para obtener los nombres de las tablas, y luuego las guardamos en la variable 'var'.
var = print(engine.table_names())
