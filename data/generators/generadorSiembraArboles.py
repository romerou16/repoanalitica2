import random

def generarDatosSiembraArboles():
    listaDatos = []

    for i in range(1000):
        corregimientos = random.choice('San Sebastián de Palmitas', 'San Cristóbal', 'Altavista', 'San Antonio de Prado', 'Santa Elena')
        hectareas = round(random.uniform(5, 20), 1)  # Genera un valor flotante entre 5 y 20 con una decimal
        especie = random.choice( 'Guayacán', 'Ceiba', 'Urapán', 'Chiminango', 'Carbonero', 'Jacarandá', 'Acacia', 'Gualanday')
        nombre = random.sample('Carlos Mejía', 'Laura Pérez', 'Andrés Torres', 'Mariana Ramírez', 'Fernando Gómez', 'Sofía Álvarez','Camilo Herrera', 'Daniela Castillo')  # Selecciona 2 nombres al azar
        fecha = random.choice('2024-05-15', '2024-06-01', '2024-04-30', '2024-03-25', '2024-05-20')
        correo = random.choice('1coreo@gmail.com','2coreo@gmail.com','3coreo@gmail.com','coreo@gmail.com')
        
        encuesta = [corregimientos, hectareas, especie, nombre, fecha, correo]
     
        
        listaDatos.append(encuesta)

    return listaDatos

