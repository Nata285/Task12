import psycopg2
import sqlalchemy


engine= sqlalchemy.create_engine('postgresql://postgres:q2w3e4r5@localhost:5432/Task4')
connection = engine.connect()

connection.execute("""INSERT INTO singer (name)
                    VALUES('Город 312'),
                          ('Алиса'),
                          ('Серега'),
                          ('Михаил Шелег'),
                          ('Ирина Ежова'),
                          ('Jazz Dance Orchestra'),
                          ('БИ-2'),
                          ('Гарик Сукачев')
                    ;""")

connection.execute("""INSERT INTO album (name, year)
                    VALUES('Вне зоны доступа', '2009'),
                           ('Цирк', '2020'),
                           ('Черный бумер', '2012'),
                           ('За Удачу!', '2017'),
                           ('Скрипач', '2013'),
                           ('No stress music', '2018'),
                           ('Горизонт событий', '2017'),
                            ('Право на выбор', '2012')
                    ;""")


