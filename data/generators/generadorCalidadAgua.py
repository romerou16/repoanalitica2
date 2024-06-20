import random

def generarDatosCalidadAgua():
    listaDatos=[]

    for i in range(1000):
        localidad = random.choice(['Chapinero', 'Usaquén', 'Teusaquillo', 'Kennedy', 'Suba'])
        fecha_muestreo = random.choice(['2024-06-01', '2024-06-02', '2024-06-03', '2024-06-04', '2024-06-05','sin'])
        turbidez = round(random.uniform(0, 150))  # Genera un valor flotante entre 0 y 5 con dos decimales (NTU)
        responsables = random.choice(['Empresa de Acueducto', 'Autoridad Ambiental', 'Universidad Local', 'ONG Ambiental'])
        correo_contacto = random.choice(['contacto1@example.com', 'contacto2@example.com', 'contacto3@example.com', 'contacto4@example.com'])

        # Crear una lista de datos para cada registro
        encuesta = [localidad, fecha_muestreo, turbidez, responsables, correo_contacto]

        # Agregar el registro a la lista principal
        listaDatos.append(encuesta)

    return listaDatos



