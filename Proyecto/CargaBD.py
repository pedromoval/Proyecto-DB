import mysql.connector as db
import csv

# creamos una nueva conexión con la base de datos creada
mydb = db.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'mysql',
    database = 'cine'
)

# Usando la conexión creamos un cursor
cursor = mydb.cursor()

with open(r'C:\Users\pmora\OneDrive\Desktop\Python_UC\Python_y_bases_de_datos\MiniProyecto_2\actors.csv',encoding="utf8") as csvfile:
    readCSV = csv.reader(csvfile, delimiter=';')
    filas = []
    first = next(readCSV)
    for row in readCSV:
        filas.append(tuple([int(row[0]), row[1], row[2]]))

sqlSentence = 'INSERT INTO actors(id, first_name, last_name) VALUES (%s, %s, %s)'
cursor.executemany(sqlSentence, filas)
print('Carga a tabla actors finalizada\n')
mydb.commit()

#2######################################

with open(r'C:\Users\pmora\OneDrive\Desktop\Python_UC\Python_y_bases_de_datos\MiniProyecto_2\directors.csv',encoding="utf8") as csvfile:
    readCSV = csv.reader(csvfile, delimiter=';')
    filas =[]
    first = next(readCSV)
    for row in readCSV:
        filas.append((int(row[0]),(row[1]),(row[2])))

sqlSentence = 'INSERT INTO directors(id, first_name, last_name)\
                                     VALUES (%s,%s,%s)'
cursor.executemany(sqlSentence, filas)
print('Carga a tabla directors finalizada\n')
mydb.commit()

#3#################################################################

with open(r'C:\Users\pmora\OneDrive\Desktop\Python_UC\Python_y_bases_de_datos\MiniProyecto_2\movies_actors.csv',encoding="utf8") as csvfile:
    readCSV = csv.reader(csvfile, delimiter=';')
    filas =[]
    first = next(readCSV)
    for row in readCSV:
        filas.append((int(row[0]), row[1], row[2]))

sqlSentence = 'INSERT INTO movies_actors(actor_id, movie_id, role) VALUES (%s,%s,%s)'
cursor.executemany(sqlSentence, filas)
print('Carga a tabla movies_actors finalizada\n')
mydb.commit()

#4##########################################################################3

with open(r'C:\Users\pmora\OneDrive\Desktop\Python_UC\Python_y_bases_de_datos\MiniProyecto_2\movies_directors.csv',encoding="utf8") as csvfile:
    readCSV = csv.reader(csvfile, delimiter=';')
    filas =[]
    first = next(readCSV)
    for row in readCSV:
        filas.append((int(row[0]), row[1]))

sqlSentence = 'INSERT INTO movies_directors(director_id, movie_id) VALUES (%s,%s)'
cursor.executemany(sqlSentence, filas)
print('Carga a tabla movies_directors finalizada\n')
mydb.commit()

#5########################################################################

with open(r'C:\Users\pmora\OneDrive\Desktop\Python_UC\Python_y_bases_de_datos\MiniProyecto_2\movies.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=';')
    filas =[]
    first = next(readCSV)
    for row in readCSV:
        filas.append((int(row[0]),(row[1]),(row[2]),row[3]))

sqlSentence = 'INSERT INTO movies(id, name, year, ranking)\
                                     VALUES (%s,%s,%s,%s)'
cursor.executemany(sqlSentence, filas)
print('Carga a tabla movies finalizada\n')
mydb.commit()
mydb.close()
cursor.close()