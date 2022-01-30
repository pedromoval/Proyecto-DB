import mysql.connector as db
import pandas as pd

# creamos una nueva conexión con la base de datos creada
mydb = db.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'mysql',
    database = 'cine'
)

# Usando la conexión creamos un cursor
cursor = mydb.cursor()

##### IMPRIMIR LAS TABLAS #####
sqlSentence = 'SELECT * FROM movies'
cursor.execute(sqlSentence)
rows = cursor.fetchall()
print('===== TABLA MOVIES =====')
for row in rows:
 print(row)

##### IMPRIMIR LAS TABLAS #####
sqlSentence = 'SELECT * FROM actors'
cursor.execute(sqlSentence)
rows = cursor.fetchall()
print('===== TABLA ACTORS =====')
for row in rows:
 print(row)

##### IMPRIMIR LAS TABLAS #####
sqlSentence = 'SELECT * FROM directors'
cursor.execute(sqlSentence)
rows = cursor.fetchall()
print('===== TABLA DIRECTORS =====')
for row in rows:
 print(row)

##### IMPRIMIR LAS TABLAS #####
sqlSentence = 'SELECT * FROM movies_actors'
cursor.execute(sqlSentence)
rows = cursor.fetchall()
print('===== TABLA MOVIES_ACTORS =====')
for row in rows:
 print(row)

##### IMPRIMIR LAS TABLAS #####
sqlSentence = 'SELECT * FROM movies_directors'
cursor.execute(sqlSentence)
rows = cursor.fetchall()
print('===== TABLA MOVIES_DIRECTORS =====')
for row in rows:
 print(row)

## 3.1 Directores que tienen más de 3 películas ordenadas en orden decreciente.

sqlSentence = 'SELECT d.last_name, d.first_name, COUNT(movie_id) as How_Many FROM movies_directors as md \
                JOIN directors as d on d.id = md.director_id \
                GROUP by d.last_name, d.first_name \
                HAVING COUNT(movie_id) > 3 \
                ORDER BY COUNT(movie_id) DESC'

cursor.execute(sqlSentence)
rows = cursor.fetchall()
lista = []
for row in rows:
    lista.append(row)
dframe= pd.DataFrame(lista, columns=['last_name','first_name','How Many'])
print(dframe)


## 3.2 Obtener el ranking de actores desplegando la cuenta de películas para todos, ordenados por apellido.

sqlSentence = 'SELECT a.last_name, a.first_name, COUNT(movie_id) \
                FROM actors as a JOIN movies_actors as ma on ma.actor_id = a.id \
                GROUP BY a.last_name, a.first_name \
                ORDER BY a.last_name, a.first_name'

cursor.execute(sqlSentence)
rows = cursor.fetchall()
lista = []
for row in rows:
    lista.append(row)
dframe1 = pd.DataFrame(lista, columns=['last_name', 'first_name', 'COUNT'])
print(dframe1)

## 3.3 espliega una lista de películas, el año, su director y el puntaje (rank) solo para las películas
##     con rank mayor a 8 ordenadas en forma decreciente.

sqlSentence = 'SELECT m.name as Movie, m.year as Year, d.last_name AS Director, \
                m.ranking as Ranking \
                FROM (movies_directors as md JOIN movies as m on m.id = md.movie_id) \
                JOIN directors as d on d.id = director_id \
                WHERE m.ranking > 8 \
                ORDER BY m.ranking DESC'

cursor.execute(sqlSentence)
rows = cursor.fetchall()
lista = []
for row in rows:
    lista.append(row)
dframe2 = pd.DataFrame(lista, columns=['Movie', 'Year', 'Director', 'Rank'])
print(dframe2)