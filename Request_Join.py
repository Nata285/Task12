import psycopg2
import sqlalchemy


engine= sqlalchemy.create_engine('postgresql://postgres:q2w3e4r5@localhost:5432/Task4')
connection = engine.connect()

res_1 = connection.execute ("""SELECT name, COUNT(name) FROM genre 
                          JOIN singer_genre ON singer_genre.genre_id = genre.id
                          GROUP BY name
                          ;""").fetchall()
print(res_1)
res_2 = connection.execute ("""SELECT album.name, album.year, COUNT(track.name) FROM track
                          JOIN album ON track.album_id = album.id
                          GROUP BY album.year, album.name
                          HAVING album.year = '2019' OR album.year = '2020'
                          ;""").fetchall()
print(res_2)

res_3 = connection.execute ("""SELECT album.name, AVG(duration) FROM track
                          JOIN album ON track.album_id = album.id
                          GROUP BY album.name
                          ;""").fetchall()
print(res_3)

res_4 = connection.execute ("""SELECT singer.name, album.year FROM singer
                          JOIN singer_album ON singer_album.singer_id = singer.id
                          JOIN album ON singer_album.album_id = album.id
                          GROUP BY singer.name, album.year 
                          HAVING album.year != '2014'
                          ;""").fetchall()
print(res_4)

res_5 = connection.execute ("""SELECT collection.name, singer.name FROM collection
                          JOIN track_collection ON track_collection.collection_id = collection.id
                          JOIN track ON track_collection.track_id = track.id
                          JOIN singer_album ON track.album_id = singer_album.album_id
                          JOIN singer ON singer.id = singer_album.singer_id
                          GROUP BY collection.name, singer.name 
                          HAVING singer.name = 'Алиса'
                          ;""").fetchall()
print(res_5)
res_6 = connection.execute ("""SELECT album.name, COUNT(genre.name) FROM album
                          JOIN singer_album ON album.id = singer_album.album_id
                          JOIN singer ON singer_album.singer_id = singer.id
                          JOIN singer_genre ON singer_genre.singer_id = singer.id
                          JOIN genre ON genre.id = singer_genre.genre_id
                          GROUP BY  album.name 
                          HAVING COUNT(genre.name)>1
                          ;""").fetchall()
print(res_6)
res_7 = connection.execute ("""SELECT track.name FROM track
                          FULL OUTER JOIN track_collection ON track.id = track_collection.track_id
                          GROUP BY  track.name 
                          
                          ;""").fetchall()
print(res_7)
res_8 = connection.execute("""SELECT singer.name, MIN(track.duration) FROM singer
                          JOIN singer_album ON singer_album.singer_id = singer.id
                          JOIN track ON singer_album.album_id = track.album_id
                          GROUP BY  singer.name, track.duration
                          HAVING duration=(SELECT MIN(duration) FROM track)
                          ;""").fetchall()
print(res_8)

res_9 = connection.execute("""SELECT album.name, COUNT(track.name)  FROM album 
                          JOIN track ON track.album_id = album.id
                          GROUP BY  album.name 
                          HAVING (SELECT MIN (COUNT(track.name))
                           FROM (SELECT album.name, COUNT(track.name)  FROM album 
                          JOIN track ON track.album_id = album.id
                          GROUP BY  album.name))
                          
                          ;""").fetchall()
print(res_9)