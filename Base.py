import psycopg2
import sqlalchemy


engine= sqlalchemy.create_engine('postgresql://postgres:q2w3e4r5@localhost:5432/Task4')
connection = engine.connect()

connection.execute("""INSERT INTO genre (name)
                    VALUES('Рок'),
                          ('Рэп'),
                          ('Шансон'),
                          ('Джаз'),
                          ('Металл')
                    ;""")



