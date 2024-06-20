import pandas as pd
import matplotlib.pyplot as plt
from data.generators.generadorResiduos import generarDatosGestionResiduos
from helpers.crearTablaHTML import crearTabla

def construirResiduosDataFrame():
    datosResiduos = generarDatosGestionResiduos()

    # Generar el DataFrame
    residuosDataFrame = pd.DataFrame(datosResiduos, columns=['localidad', 'fecha_recoleccion', 'tipo_residuo', 'cantidad_recolectada', 'responsables', 'correo_contacto'])

    # Limpiar el DataFrame si hay valores 'sin'
    residuosDataFrame.replace('sin', pd.NA, inplace=True)
    #elimino los registros que no cumplen el criterio
    residuosDataFrame.dropna(inplace=True)

    # Filtrar los datos según la cantidad recolectada
   
    cantidadesBajas = residuosDataFrame.query("(cantidad_recolectada>=0)and(cantidad_recolectada<40)").value_counts()
    cantidadesregulares = residuosDataFrame.query("(cantidad_recolectada>=41)and(cantidad_recolectada<80)").value_counts()
    cantidadesAltas = residuosDataFrame.query("(cantidad_recolectada>=81)and(cantidad_recolectada<100)").value_counts()

    
    # print(cantidadesBajas)
    # print("\n")
    # print(cantidadesregulares)
    # print("\n")
    # print(cantidadesAltas)
    datosOrdenadosResiduos=residuosDataFrame.groupby('localidad')['cantidad_recolectada'].mean()
    print(datosOrdenadosResiduos)

    datosOrdenadosResiduos.plot(kind='bar',color='green')
    plt.title("Indice por contaminacion de residuos por localidad en medellin")
    plt.xlabel("localidad")
    plt.ylabel("cantidad_recolectada")
    plt.grid(True)
    plt.savefig("./assets/img/calidadaire.png",format='png',dpi=300)

    
    plt.show()

# Ejecutar la función para construir y analizar el DataFrame de Gestión de Residuos
construirResiduosDataFrame()
