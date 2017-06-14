# Importamos la función create_engine
from sqlalchemy import create_engine

# Creamos un engine apuntando a la base de datos elegida. En este caso, census DB. 
# El ejemplo utiliza una DB PostgreSQL alojada en la nube de Amazon.
engine = create_engine('postgresql+psycopg2://student:datacamp@postgresql.csrrinzqubik.us-east-1.rds.amazonaws.com:5432/census')

# Usamos el método .table_names() en el engine para imprimir en pantalla los nombres de las tablas.
print(engine.table_names())
