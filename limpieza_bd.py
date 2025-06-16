#Este archivo existe en el proyecto sólo para mostrar los códigos donde logré limpiar una base de datos (title.basics.tsv.gz) con más de 11 millones de filmes (documentales,episodios,tvShows,etc,etc)
#En dos archivos tsv (películas.tsv y series.tsv), reduciendo la muestra a poco más de un millón de filmes y optimizando el manejo de datos del proyecto
import pandas as p

ruta_archivo = "title.basics.tsv.gz"
BD = p.read_csv(ruta_archivo , sep='\t', compression='gzip' , low_memory= False)
Bd = BD.to_dict("records")
BD_peliculas = [i for i in Bd if i['titleType'] == "movie"]
for i in BD_peliculas:
    i["startYear"] = p.to_numeric(i["startYear"] , errors= 'coerce')
    i["runtimeMinutes"] = p.to_numeric(i["runtimeMinutes"] , errors= 'coerce')

BD_series = [i for i in Bd if i["titleType"] == "tvSeries"]
for i in BD_series:
    i["startYear"] = p.to_numeric(i["startYear"], errors= 'coerce')
    i["endYear"] = p.to_numeric(i["endYear"], errors='coerce')

ar_peliculas = p.DataFrame(BD_peliculas)
ar_series = p.DataFrame(BD_series)
ar_peliculas.to_csv("peliculas.tsv", sep= "\t", index=False)
ar_series.to_csv("series.tsv", sep="\t", index=False)

#Aunque tarda un poco (lógicamente) resultó ser bastante efectivo en la realización del proyecto