import psycopg2
import sqlalchemy


engine= sqlalchemy.create_engine('postgresql://postgres:q2w3e4r5@localhost:5432/Task3')
connection = engine.connect()
res_1 = connection.execute ("""SELECT name, year FROM album
                          WHERE year = '2018';""").fetchall()
print(res_1)

res_2 = connection.execute ("""SELECT name, duration FROM track
                          ORDER BY duration DESC;;""").fetchall()
print(res_2[0])
res_3 = connection.execute ("""SELECT name, duration FROM track
                          WHERE duration > '3.5';""").fetchall()
print(res_3)
res_4 = connection.execute ("""SELECT name, year FROM collection
                          WHERE year BETWEEN '2018' AND '2020';""").fetchall()
print(res_4)
res_5 = connection.execute ("""SELECT name FROM singer
                          WHERE name NOT LIKE '%% %%';""").fetchall()
print(res_5)
res_6 = connection.execute ("""SELECT name FROM singer
                          WHERE name  LIKE '%%мой/my%%';""").fetchall()
print(res_6)