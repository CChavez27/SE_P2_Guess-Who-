import json

# Cargar los componentes desde un archivo JSON
def cargar_componentes(archivo="componentes.json"):
    try:
        with open(archivo, "r") as f:
            componentes = json.load(f)
    except FileNotFoundError:
        componentes = {}
    return componentes

# Guardar los componentes en un archivo JSON
def guardar_componentes(componentes, archivo="componentes.json"):
    with open(archivo, "w") as f:
        json.dump(componentes, f, indent=4)

# Definir o cargar los componentes existentes
componentes = cargar_componentes()

if not componentes:  # Si no hay componentes, inicializar algunos
    componentes = {
        "Resistor": {"Es pasivo": True, "Tiene polaridad": False, "Regula corriente": True, "Almacena energía": False},
        "Capacitor": {"Es pasivo": True, "Tiene polaridad": False, "Regula corriente": False, "Almacena energía": True},
        "Diodo": {"Es activo": True, "Tiene polaridad": True, "Regula corriente": True, "Almacena energía": False},
        "Transistor": {"Es activo": True, "Tiene polaridad": True, "Regula corriente": True, "Almacena energía": False},
    }
    guardar_componentes(componentes)  # Guardar componentes por primera vez

# Función para hacer preguntas al usuario
def adivina_componente():
    posibles = componentes.copy()  # Copia de todos los componentes posibles
    while len(posibles) > 1:
        # Elegir una característica sobre la cual preguntar
        caracteristica = list(posibles.values())[0].keys()  # Usar la primera característica
        for c in caracteristica:
            respuesta = input(f"¿{c}? (sí/no): ").strip().lower()
            if respuesta == 'sí':
                posibles = {k: v for k, v in posibles.items() if c in v and v[c] is True}
            else:
                posibles = {k: v for k, v in posibles.items() if c in v and v[c] is False}
            break

    # Si queda solo un componente, adivinar
    if posibles:
        print(f"El componente es: {list(posibles.keys())[0]}")
    else:
        print("No pude adivinar el componente.")
        aprender_nuevo_componente()

# Función para aprender un nuevo componente
def aprender_nuevo_componente():
    nuevo_componente = input("¿Cuál era el componente?: ")
    if nuevo_componente in componentes:
        print("Ese componente ya está registrado.")
        return
    
    nuevas_caracteristicas = {}
    continuar = True
    while continuar:
        caracteristica = input(f"Ingrese una característica para {nuevo_componente}: ")
        respuesta = input(f"¿{nuevo_componente} tiene {caracteristica}? (sí/no): ").strip().lower()
        nuevas_caracteristicas[caracteristica] = True if respuesta == 'sí' else False
        continuar = input("¿Agregar otra característica? (sí/no): ").strip().lower() == 'sí'
    
    componentes[nuevo_componente] = nuevas_caracteristicas
    guardar_componentes(componentes)
    print(f"{nuevo_componente} ha sido agregado a la base de datos.")

adivina_componente()
