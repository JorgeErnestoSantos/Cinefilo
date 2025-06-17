import matplotlib.pyplot as plt
from collections import defaultdict

class analizador_pelis:
    def __init__(self, pelis:list) -> None:
        self.pelis = pelis
    def graf_genero_año (self, año: int):
        pelis_año = []
        for i in self.pelis:
            if i.año_estreno == año:
                pelis_año.append(i)
        generos_año = defaultdict(int)
        for i in pelis_año:
            if i.generos!= []:
                for j in i.generos:
                    generos_año[j] += 1
        plt.figure(figsize=(15, 7))
        barras = plt.bar (generos_año.keys(), generos_año.values(), color='#1f77b4', width=0.6 )
        plt.title('Películas por género', fontsize=14, pad=20)
        plt.xlabel('Género', fontsize=12)
        plt.ylabel('Cantidad de películas', fonsize=12)
        plt.xticks(rotation=45, ha='right')
        plt.grid(axis='y', linestyle='--', alpha=0.4)
        for bar in barras:
            height = bar.get_height()
            plt.text(bar.get_x() + bar.get_width()/2, height , f'{height:,}', ha='center', va='bottom', fontsize=10)
        plt.tight_layout()
        plt.show
    def mayor_duración (self, año: int):
        n = ""
        a = 0
        for i in self.pelis:
            if i.año_estreno == año:
                if i.duracion != None:
                    if i.duracion >= a:
                        a = i.duracion
                        n = i.nombre
        print (f"{n}:{a} minutos")
    def menor_duraciom (self, año):
        n = self.pelis[0].nombre
        a = self.pelis[0].duracion
        for i in self.pelis:
            if i.año_estreno == año:
                if i.duracion != None:
                    if i.duracion <= a:
                        a = i.duracion
                        n = i.nombre
        print (f"{n}: {a} minutos")