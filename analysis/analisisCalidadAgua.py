import pandas as pd
import matplotlib.pyplot as plt

from data.generators.generadorCalidadAgua import generarDatosCalidadAgua
from helpers.crearTablaHTML import crearTabla

def construirAguaDataFrame():
    # Generar datos de calidad del agua
    datosAgua = generarDatosCalidadAgua()


    # Generar el DataFrame
    aguaDataFrame = pd.DataFrame(datosAgua,columns=['localidad', 'fecha_muestreo', 'turbidez', 'responsables', 'correo_contacto'])

    # Limpiar el DataFrame si hay valores 'sin'
    aguaDataFrame.replace('sin', pd.NA, inplace=True)
    aguaDataFrame.dropna(inplace=True)

    # Filtrar los datos
    # Filtrar es aplicar condiciones lógicas que permitan analizar la información del DataFrame
    filtroCalidadAguaBuena = aguaDataFrame.query("(turbidez>=0)and(turbidez<50)").value_counts()
    filtroCalidadAguaRegular = aguaDataFrame.query("(turbidez>=51)and(turbidez<100)").value_counts()
    filtroCalidadAguaMala = aguaDataFrame.query("(turbidez>=101)and(turbidez<150)").value_counts()
    
   

    # print(filtroCalidadAguaBuena.shape[0])
    # print("\n")
    # print(filtroCalidadAguaRegular.shape[0])
    # print("\n")
    # print(filtroCalidadAguaMala.shape[0])

    datosOrdenadosAgua=aguaDataFrame.groupby('localidad')['turbidez'].mean()
    print(datosOrdenadosAgua)

    datosOrdenadosAgua.plot(kind='bar',color='green')
    plt.title("Indice por contaminacion del agua por localidad en medellin")
    plt.xlabel("localidad")
    plt.ylabel("turbidez")
    plt.grid(True)
    
    plt.show()
    
    plt.savefig("./assets/img/calidadaire.png",format='png',dpi=300)

    
construirAguaDataFrame()
