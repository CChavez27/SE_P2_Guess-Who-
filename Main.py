import json
import os

# Archivo JSON donde se guardará la base de datos
archivo_bd = 'componentes.json'

# Cargar base de datos de componentes electrónicos
def cargar_componentes():
    if os.path.exists(archivo_bd):
        with open(archivo_bd, 'r') as archivo:
            return json.load(archivo)
    else:
        # Si el archivo no existe, se crea una base de datos inicial
        return [
            {'nombre': 'Resistencia', 'pines': 2, 'tipo': 'pasivo', 'color': 'varios', 'funcion': 'reducir corriente'},
            {'nombre': 'Transistor', 'pines': 3, 'tipo': 'activo', 'color': 'negro', 'funcion': 'amplificar'},
            {'nombre': 'Condensador', 'pines': 2, 'tipo': 'pasivo', 'color': 'varios', 'funcion': 'almacenar carga'},
            {'nombre': 'Diodo', 'pines': 2, 'tipo': 'activo', 'color': 'negro', 'funcion': 'permitir paso en un sentido'}
        ]

# Guardar la base de datos de componentes electrónicos
def guardar_componentes(componentes):
    with open(archivo_bd, 'w') as archivo:
        json.dump(componentes, archivo, indent=4)

# Función para hacer preguntas y filtrar componentes
def hacer_pregunta(componentes, caracteristica, valor):
    return [comp for comp in componentes if comp[caracteristica] == valor]

# Función principal para adivinar el componente
def adivinar_componente(componentes):
    candidatos = componentes
    preguntas = ['pines', 'tipo', 'color', 'funcion']
    
    for pregunta in preguntas:
        opciones = list(set(comp[pregunta] for comp in candidatos))
        if len(opciones) == 1:
            continue
        
        respuesta = input(f"¿Tu componente tiene {pregunta} igual a '{opciones[0]}'? (s/n): ").lower()
        if respuesta == 's':
            candidatos = hacer_pregunta(candidatos, pregunta, opciones[0])
        else:
            candidatos = hacer_pregunta(candidatos, pregunta, opciones[1] if len(opciones) > 1 else opciones[0])
        
        if len(candidatos) == 1:
            break

    if len(candidatos) == 1:
        print(f"¡Tu componente es un {candidatos[0]['nombre']}!")
    else:
        print("No logré adivinar tu componente.")
        nuevo_componente = {}
        for pregunta in preguntas:
            nuevo_componente[pregunta] = input(f"¿Cuál es el {pregunta} de tu componente?: ")
        nuevo_componente['nombre'] = input("¿Cuál es el nombre de tu componente?: ")
        componentes.append(nuevo_componente)
        guardar_componentes(componentes)
        print("Gracias, he aprendido un nuevo componente.")

# Ejecutar el juego
componentes = cargar_componentes()
print("Piensa en un componente electrónico...")
adivinar_componente(componentes)
