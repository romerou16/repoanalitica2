import pandas as pd
from data.generators.generadorSiembraArboles import generarDatosSiembraArboles
from helpers.crearTablaHTML import crearTabla

def construirSiembraArbolesDataFrame():
    datosSiembraArboles=generarDatosSiembraArboles()

    #generamos el dataframe
    siembraArbolesDataFrame=pd.DataFrame(datosSiembraArboles,columns=['corregimientos', 'hectareas', 'especie', 'nombre', 'fecha', 'correo'])

    #crearTabla(siembraArbolesDataFrame,"datoSiembraArboles")
    #Limpiando el dataframe
    #reemplazando valores 
    siembraArbolesDataFrame.replace('sin',pd.NA,inplace=True)
    #elimino los registros que no cumplen el criterio
    siembraArbolesDataFrame.dropna(inplace=True)
    
    #filtrar DATOS
    #Filtrar es aplicar condiciones logicas
    #que permitan analizar la informacion del DF
    hectareas_bajas = siembraArbolesDataFrame[siembraArbolesDataFrame['hectareas'] < 10].count()
    hectareas_medias = siembraArbolesDataFrame[(siembraArbolesDataFrame['hectareas'] >= 10) & (siembraArbolesDataFrame['hectareas'] < 15)].count()
    hectareas_altas = siembraArbolesDataFrame[siembraArbolesDataFrame['hectareas'] >= 15].count()

    print("Cantidad de registros con menos de 10 hectáreas sembradas:")
    print(hectareas_bajas)
    print("\n")
    print("Cantidad de registros con 10-15 hectáreas sembradas:")
    print(hectareas_medias)
    print("\n")
    print("Cantidad de registros con más de 15 hectáreas sembradas:")
    print(hectareas_altas)

# Ejecutar la función para construir y analizar el DataFrame de Siembra de Árboles
construirSiembraArbolesDataFrame()