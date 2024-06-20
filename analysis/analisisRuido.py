import pandas as pd
from data.generators.generadorRuidoAmbiental import generarDatosRuidoAmbiental
from helpers.crearTablaHTML import crearTabla

# Función para construir y analizar el DataFrame de ruido ambiental
def construirRuidoDataFrame():
    datosRuido = generarDatosRuidoAmbiental()

    # Generar el DataFrame
    ruidoDataFrame = pd.DataFrame(datosRuido, columns=['comuna', 'direccion', 'nombre', 'decibelios_diurnos', 'decibelios_nocturnos', 'fecha'])

   #crearTabla(aireDataFrame,"datosaire")
    #Limpiando el dataframe
    #reemplazando valores 
    ruidoDataFrame.replace('sin',pd.NA,inplace=True)
     #elimino los registros que no cumplen el criterio
    ruidoDataFrame.dropna(inplace=True)

   #filtrar DATOS
    #Filtrar es aplicar condiciones logicas
    #que permitan analizar la informacion del DF
    filtroRuidoDiurnoAlto = ruidoDataFrame.query("decibelios_diurnos >= 70").value_counts()
    filtroRuidoDiurnoMedio = ruidoDataFrame.query("decibelios_diurnos >= 60 and decibelios_diurnos < 70").value_counts()
    filtroRuidoDiurnoBajo = ruidoDataFrame.query("decibelios_diurnos < 60").value_counts()

    filtroRuidoNocturnoAlto = ruidoDataFrame.query("decibelios_nocturnos >= 60").value_counts()
    filtroRuidoNocturnoMedio = ruidoDataFrame.query("decibelios_nocturnos >= 50 and decibelios_nocturnos < 60").value_counts()
    filtroRuidoNocturnoBajo = ruidoDataFrame.query("decibelios_nocturnos < 50").value_counts()

 
    print(filtroRuidoDiurnoAlto)
    print("\n")
    print(filtroRuidoDiurnoMedio)
    print("\n")
    print(filtroRuidoDiurnoBajo)
    
    
    print(filtroRuidoNocturnoAlto)
    print("\n")
    print(filtroRuidoNocturnoMedio)
    print("\n")
    print(filtroRuidoNocturnoBajo)

# Ejecutar la función para construir y analizar el DataFrame de ruido ambiental
construirRuidoDataFrame()