import pandas as p

#Extracción de datos de las películas#

class Pelicula:
    def __init__(self, nombre , nombre_original , generos , año_estreno , duracion) -> None:
        self.nombre = nombre
        self.nombre_original = nombre_original
        self.generos = generos
        self.año_estreno = año_estreno
        self.duracion = duracion

ruta_archivo = "peliculas.tsv"
BD = p.read_csv(ruta_archivo , sep='\t', low_memory= False)
Bd = BD.to_dict("records")
for i in Bd:
    i["startYear"] = p.to_numeric(i["startYear"] , errors= 'coerce')
    i["runtimeMinutes"] = p.to_numeric(i["runtimeMinutes"] , errors= 'coerce')
lista_peliculas = []
for i in Bd:
    pelicula = Pelicula (nombre=i["primaryTitle"] , nombre_original=i["originalTitle"] , generos=i["genres"].split(',') if p.notna(i["genres"]) else [], año_estreno= int(i["startYear"]) if p.notna(i["startYear"]) else None , duracion= int(i["runtimeMinutes"]) if p.notna(i["runtimeMinutes"]) else None)
    lista_peliculas.append(pelicula)


#Extracción de las series#
class Serie:
    def __init__(self, nombre, nombre_original , generos , año_inicio , año_fin) -> None:
        self.nombre = nombre
        self.nombre_original = nombre_original
        self.generos = generos
        self.año_inicio = año_inicio
        self.año_fin = año_fin

ruta_archivo = "series.tsv"
BD = p.read_csv(ruta_archivo, sep="\t", low_memory= False)
Bd = BD.to_dict("records")
for i in Bd:
    i["startYear"] = p.to_numeric(i["startYear"], errors= 'coerce')
    i["endYear"] = p.to_numeric(i["endYear"], errors='coerce')
lista_series = []
for i in Bd:
    serie = Serie (nombre= i["primaryTitle"], nombre_original= i["originalTitle"], generos= i["genres"] if p.notna(i["genres"]) else [] , año_inicio= int(i["startYear"]) if p.notna(i["startYear"]) else None , año_fin= int(i["endYear"]) if p.notna(i["endYear"]) else None)
    lista_series.append(serie) 

 