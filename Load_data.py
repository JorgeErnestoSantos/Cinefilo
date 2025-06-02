import pandas as p

#Extracción de datos de las películas#

class Pelicula:
    def __init__(self, nombre , nombre_original , generos , año_estreno , duracion) -> None:
        self.nombre = nombre
        self.nombre_original = nombre_original
        self.generos = generos
        self.año_estreno = año_estreno
        self.duracion = duracion

ruta_archivo = "title.basic.tsv.gz"
BD = p.read_csv(ruta_archivo , sep='\t', compression='gzip' , low_memory= False)
BD_peliculas = BD[BD['titleType'] == 'movie'].copy()

BD_peliculas['startYear'] = p.to_numeric(BD_peliculas['startYear'] , errors= 'coerce')
BD_peliculas['runtimeMinutes'] = p.to_numeric(BD_peliculas['runtimeMinutes'] , errors= 'coerce')

lista_peliculas = []
for _, row in BD_peliculas.iterrows():
    pelicula = Pelicula (nombre=row['primaryTitle'] , nombre_original=row['originalTitle'] , generos=row['genres'].split(',') if p.notna(row['genres']) else [], año_estreno= int(row['startYear'] if p.notna(row['startYear']) else None) , duracion= int(row['runtimeMinutes']) if p.notna(row['runtimeMinutes']) else None)
    lista_peliculas.append(pelicula)


#Extracción de las series#
class Serie:
    def __init__(self, nombre, nombre_original , generos , año_inicio , año_fin) -> None:
        self.nombre = nombre
        self.nombre_original = nombre_original
        self.generos = generos
        self.año_inicio = año_inicio
        self.año_fin = año_fin

BD_series = BD[BD['titleType'] == 'tvSeries'].copy()
BD_series['startYear'] = p.to_numeric(BD_series['startYear'], errors= 'coerce')
BD_series['endYear'] = p.to_numeric(BD_series['endYear'], errors='coerce')

lista_series = []
for _,row in BD_series:
    serie = Serie (nombre= row['primaryTitle'], nombre_original= row['originalTitle'], generos= row['genre'] if p.notna(row['genre']) else [] , año_inicio= row['startYear'] if p.notna(row['startYear']) else None , año_fin= row['endYear'] if p.notna(row['endYear']) else None)
    lista_series.append(serie)

 