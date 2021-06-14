import psycopg2
import sqlalchemy

engine = sqlalchemy.create_engine('postgresql://postgres:q2w3e4r5@localhost:5432/Task4')
connection = engine.connect()

connection.execute("""INSERT INTO track (name,duration,album_id)
                    VALUES('Останусь на всегда', 2.5, 1),
                          ('Поговори со мной еще', 3.0, 1)
                         
                    ;""")
