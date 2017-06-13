from sqlalchemy import create_engine, MetaData, Table
from Pandas import 
from mathplotlib import 

#Create SQLAlchemy engine
engine = create_engine ('Driver+Dialect:///Filename')
metadata = MetaData()

#Store the connection method
connection = engine.connect()

#Print out table names
print(engine.table_names())

#Reflect the table 'TableName' and store metadata in 'tablePrint'
tablePrint = Table('TableName', metadata, autoload=True, autoload_with=engine)

#Print out metadata of 'tableName'
print(repr('tablePrint'))

# Print the column names
print(tablePrint.columns.keys())

# Print full table metadata
print(repr(metadata.tables['TableName']))

#SQLAlchemy querying. select = SELECT * FROM [TableName]
stmt = select([TableName])
print(stmt)

#ResultProxy
result_proxy = connection.execute(stmt)

#ResultSet
results = result_proxy.fetchall()

