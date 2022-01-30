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

## Ejercicio numero 4

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
df1 = pd.DataFrame(lista, columns=['Pelicula', 'Agno', 'Director', 'Puntaje'])
print(df1)

## Recorte ese dataframe usando loc de modo de tomar solo las primeras 10
## filas y solo las columnas Película y Puntaje. Imprima el nuevo Dataframe
## resultante.

slicing = df1.loc[:10,['Pelicula','Puntaje']]
print(slicing)


## Recorte nuevamente df1 ahora usando iloc de modo de tomar las filas 20 a
## la 50 y todas las columnas. Imprima el nuevo Dataframe resultante.

slicing1 = df1.iloc[20:51,:]
print(slicing1)