import psycopg2
import sqlalchemy


engine= sqlalchemy.create_engine('postgresql://postgres:q2w3e4r5@localhost:5432/Task3')
connection = engine.connect()
connection.execute("""INSERT INTO collection (name, year)
                    VALUES('сборник № 1',2017),
                          ('сборник № 2', 2018),
                          ('сборник № 3',2018),
                          ('сботник № 4', 2019),
                          ('сборник № 5',2020),
                          ('сборник № 6',2021),
                          ('сбоник № 7', 2016),
                          ('сборник № 8',2015)
                    ;""")
connection.execute("""INSERT INTO singer_album (singer_id,album_id)
                    VALUES(1,1),
                          (2,2),
                          (3,3),
                          (4,4),
                          (5,5),
                          (6,6),
                          (7,7),
                          (8,8)
                    ;""")
connection.execute("""INSERT INTO singer_genre (singer_id,genre_id)
                    VALUES(1,2),
                          (2,2),
                          (3,3),
                          (4,4),
                          (5,4),
                          (6,5),
                          (7,6),
                          (8,6)
                    ;""")
connection.execute("""INSERT INTO track_collection (track_id,collection_id)
                    VALUES(24,1),
                          (21,1),
                          (17,2),
                          (18,2),
                          (11,3),
                          (6,3),
                          (5,4),
                          (7,4),
                          (8,5),
                          (9,5),
                          (18,6),
                          (11,6),
                          (8,6),
                          (6,6),
                          (16,7),
                          (7,7),
                          (5,7),
                          (13,7),
                          (19,8),
                          (12,8),
                          (5,8),
                          (73,8)
                    ;""")