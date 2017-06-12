from sqlalchemy import create_engine, MetaData, Table

#Create SQLAlchemy engine
engine = create_engine ('Driver+Dialect:///Filename')
metadata = MetaData()

#Store the connection method
connection = engine.connect()

#Print out table names
print(engine.table_names())

#Store metadata of 'tableName'
tablePrint = Table('TableName', metadata, autoload=True, autoload_with=engine)

#Print out metadata of 'tableName'
print(repr('tablePrint'))

# Print the column names
print(tablePrint.columns.keys())

# Print full table metadata
print(repr(metadata.tables['TableName']))

#Basic SQL querying
stmt = 'SELECT * FROM "TableName"'

#ResultProxy
result_proxy = connection.execute(stmt)

#ResultSet
results = result_proxy.fetchall()

