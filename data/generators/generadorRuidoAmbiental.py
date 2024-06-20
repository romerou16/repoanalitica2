import random

def generarDatosRuidoAmbiental():
    listaDatos = []

    
    for i in range(1000):
        nombre = random.choice('Ana Pérez', 'José Jimeno', 'Marco Polo', 'Martha Lucrecia', 'Karen Andrea')
        comuna = random.randint(1, 14)
        direccion = random.choice('Calle 1', 'Avenida Principal', 'Carrera 9', 'Calle 45', 'Avenida del Sol', 'Calle de la Luna')
        decibelios_diurnos = round(random.uniform(50.0, 80.0), 2)  # Genera un valor flotante entre 50 y 80
        decibelios_nocturnos = round(random.uniform(40.0, 70.0), 2)  # Genera un valor flotante entre 40 y 70
        fecha = random.choice('2024-05-15', '2024-05-16', '2024-05-17')
        
        # Crear una lista de datos para cada registro
        encuesta = [comuna, direccion, nombre, decibelios_diurnos, decibelios_nocturnos, fecha]
        
        # Agregar el registro a la lista principal
        listaDatos.append(encuesta)
    
    return listaDatos

