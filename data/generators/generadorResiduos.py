import random

def generarDatosGestionResiduos():
    listaDatos = []

    for i in range(1000):
        localidad = random.choice(['Kennedy', 'Usaquén', 'Chapinero', 'Teusaquillo', 'Engativá'])
        fecha_recoleccion = random.choice(['2024-06-01', '2024-06-02', '2024-06-03', '2024-06-04', '2024-06-05'])
        tipo_residuo = random.choice(['Plástico', 'Papel', 'Vidrio', 'Orgánico', 'Electrónico'])
        cantidad_recolectada = round(random.uniform(10, 100))  # Genera un valor flotante entre 10 y 100 con dos decimales
        responsables = random.choice(['Empresa de Servicios Públicos', 'ONG Ambiental', 'Voluntarios del Barrio', 'Asociación de Recicladores'])
        correo_contacto = random.choice(['contacto1@example.com', 'contacto2@example.com', 'contacto3@example.com', 'contacto4@example.com'])

        # Crear una lista de datos para cada registro
        encuesta = [localidad, fecha_recoleccion, tipo_residuo, cantidad_recolectada, responsables, correo_contacto]

        # Agregar el registro a la lista principal
        listaDatos.append(encuesta)

    return listaDatos
