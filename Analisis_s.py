import matplotlib.pyplot as plt
from collections import defaultdict
class analizador_series:
    def __init__ (self, series:list):
        self.series = series
    def graf_genero_año (self, año):
        series_año = []
        for i in self.series:
            if i.año_inicio != None and i.año_fin != None:
                if i.año_inicio <= año and i.año_fin >= año:
                    series_año.append(i)
        generos_año = defaultdict(int)
        for i in series_año:
            if i.generos != []:
                for j in i.generos:
                    generos_año[j] += 1
        plt.figure(figsize=(15, 7))
        barras = plt.bar (generos_año.keys(), generos_año.values(), color='#1f77b4', width=0.6 )
        plt.title('Series por género', fontsize=14, pad=20)
        plt.xlabel('Género', fontsize=12)
        plt.ylabel('Cantidad de series')
        plt.xticks(rotation=45, ha='right')
        plt.grid(axis='y', linestyle='--', alpha=0.4)
        for bar in barras:
            height = bar.get_height()
            plt.text(bar.get_x() + bar.get_width()/2, height , f'{height:,}', ha='center', va='bottom', fontsize=10)
        plt.tight_layout()
        plt.show
    def año_emision (self):
        años = defaultdict(int)
        for i in self.series:
            if i.año_inicio != None:
                c = i.año_inicio
                b = i.año_inicio
                a = i.año_inicio
                años[i.año_inicio] += 1
        for i in años.items():
            if i [1] != None:    
                if i[1] >= años[c]:
                    a = b
                    b = c
                    c = i[0]
        return f"{c}: {años[c]} series, {b}: {años[b]} series, {a}: {años[a]} series"
    def año_finalizacion (self):
        años = defaultdict(int)
        for i in self.series:
            if i.año_fin != None:
                c = i.año_fin
                b = i.año_fin
                a = i.año_fin
                años[i.año_fin] += 1
        for i in años.items():
            if i[1] != None:   
                if i[1] >= años[c]:
                    a = b
                    b = c
                    c = i[0]
        return f"{c}: {años[c]} series, {b}: {años[b]} series, {a}: {años[a]} series"