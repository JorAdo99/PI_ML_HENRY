from fastapi import FastAPI
import pandas as pd
from ast import literal_eval

df= pd.read_csv('data.csv')
app= FastAPI()
def convert_to_list(x):
        try:
            return literal_eval(x)
        except (ValueError, SyntaxError):
            return [] 
        
def filtrar_por_año(Año):
    Año_str = str(Año)  # Convertir el año a una cadena (str)
    return df[df['release_date'].str.contains(Año_str, na=False)]

# Endpoint: /genero/
@app.get('/genero/')
def genero(Año: str):
    df_filtrado = filtrar_por_año(Año) 
    df_filtrado['genres'] = df_filtrado['genres'].apply(convert_to_list)    
    df_filtrado['genres'] = df_filtrado['genres'].apply(lambda x: x if x != 0 else '')
    genero_contado={}
    for i in df_filtrado['genres']:
        for j in i :
            genero_contado[j]= genero_contado.get(j,0)+1

    generos_mas_vendidos = sorted(genero_contado , key=genero_contado.get, reverse=True)[:5] # Ordenar de mayor a menor y tomar los 3 primeros

    return generos_mas_vendidos





