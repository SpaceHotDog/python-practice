# Importamos dependencias.
from sqlalchemy import create_engine

# Creamos un engine apuntando a la base de datos elegida. En este caso, 'census'. 
# El ejemplo utiliza una DB PostgreSQL alojada en AWS.
engine = create_engine('postgresql+psycopg2://student:datacamp@postgresql.csrrinzqubik.us-east-1.rds.amazonaws.com:5432/census')

# Usamos el método .table_names() sobre el engine para guardar los nombres de las tablas en la variable 'var'.
var = print(engine.table_names())
