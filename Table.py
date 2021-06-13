import psycopg2
import sqlalchemy


engine= sqlalchemy.create_engine('postgresql://postgres:q2w3e4r5@localhost:5432/Task3')
connection = engine.connect()

connection.execute("""INSERT INTO singer (name)
                    VALUES('Город 312');""")
connection.execute("""INSERT INTO singer (name)
                    VALUES('Алиса');""")
connection.execute("""INSERT INTO singer (name)
                    VALUES('Серега');""")
connection.execute("""INSERT INTO singer (name)
                    VALUES('Михаил Шелег');""")
connection.execute("""INSERT INTO singer (name)
                    VALUES('Ирина Ежова');""")
connection.execute("""INSERT INTO singer (name)
                    VALUES('Jazz Dance Orchestra');""")
connection.execute("""INSERT INTO singer (name)
                    VALUES('БИ-2');""")
connection.execute("""INSERT INTO singer (name)
                    VALUES('Гарик Сукачев');""")

connection.execute("""INSERT INTO album (name, year)
                    VALUES('Вне зоны доступа', '2009');""")
connection.execute("""INSERT INTO album (name, year)
                    VALUES('Цирк', '2014');""")
connection.execute("""INSERT INTO album (name, year)
                    VALUES('Черный бумер', '2012');""")
connection.execute("""INSERT INTO album (name, year)
                    VALUES('За Удачу!', '2017');""")
connection.execute("""INSERT INTO album (name, year)
                    VALUES('Скрипач', '2013');""")
connection.execute("""INSERT INTO album (name, year)
                    VALUES('No stress music', '2018');""")
connection.execute("""INSERT INTO album (name, year)
                    VALUES('Горизонт событий', '2017');""")
connection.execute("""INSERT INTO album (name, year)
                    VALUES('Право на выбор', '2012');""")


