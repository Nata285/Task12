import psycopg2
import sqlalchemy


engine= sqlalchemy.create_engine('postgresql://postgres:q2w3e4r5@localhost:5432/Task3')
connection = engine.connect()

connection.execute("""INSERT INTO genre (name)
                    VALUES('Рок');""")
connection.execute("""INSERT INTO genre (name) 
                    VALUES('Рэп');""")
connection.execute("""INSERT INTO genre (name)
                    VALUES('Шансон');""")
connection.execute("""INSERT INTO genre (name)
                    VALUES('Джаз');""")
connection.execute("""INSERT INTO genre (name)
                    VALUES('Металл');""")



