import random
import tkinter as tk
from tkinter import messagebox

# Datos del juego
personajes = [
    {"nombre": "Mercy Skye", "profesion": "Hacker independiente"},
    {"nombre": "Blade Kuro", "profesion": "Mercenario cibernético"},
    {"nombre": "Dr. Nyx Lazarus", "profesion": "Científico de bioingeniería"},
    {"nombre": "Nova Chrome", "profesion": "Artista tecnoradical"},
    {"nombre": "Cypher Kane", "profesion": "Agente de seguridad corporativo"}
]

locaciones = {
    "Refugio de hackers": "Un escondite subterráneo lleno de hardware ilegal y cables colgando.",
    "Penthouse de la megacorporación": "Una suite de lujo en lo alto de una torre, con vistas de toda la ciudad.",
    "Laboratorio de modificación cibernética": "Un taller oscuro lleno de implantes y dispositivos experimentales.",
    "Bazar del mercado negro": "Un lugar clandestino donde se trafica con tecnología prohibida.",
    "Rascacielos abandonado": "Un edificio en ruinas, con pisos colapsados y graffiti en las paredes."
}

armas = ["Virus neural", "Katana de plasma", "Pistola de pulso", "Implante explosivo", "Drone sigiloso"]

# Selección aleatoria de culpable, arma y locación
culpable = random.choice(personajes)
arma_seleccionada = random.choice(armas)
locacion_seleccionada = random.choice(list(locaciones.keys()))

resultados_investigacion = [
    "Encuentras datos encriptados en un dispositivo portátil abandonado.",
    "Ves una grabación borrosa de seguridad que muestra una figura encapuchada entrando al área.",
    "Un dron espía detectó señales de actividad sospechosa en el lugar del crimen.",
    "Hay rastros de sangre en un teclado y manchas en el piso.",
    "Las cámaras de la megatorre muestran una sombra sospechosa en el laboratorio.",
    "Alguien dejó huellas digitales en un implante, registradas en el sistema de seguridad.",
    "Una grabación hackeada muestra una figura oculta cerca de la escena del crimen."
]

respuestas_inocente = [
    "Mi actividad estuvo registrada en el sistema, puedes verificarlo.",
    "Tuve un encuentro programado en el Bazar del mercado negro, tengo testigos.",
    "Mis implantes muestran que estaba en la otra parte de la ciudad en ese momento.",
    "Puedo mostrarte los logs de seguridad que demuestran mi inocencia.",
    "No tengo motivo, mi trabajo depende de mantener la seguridad del sistema."
]

respuestas_culpable = [
    "No puedo recordar exactamente, estaba... distraído.",
    "Esa noche no fui yo, hay muchos que querrían culparme.",
    "Te diré lo que sea, pero no tengo nada que ver con eso.",
    "No sé cómo mis huellas digitales aparecieron ahí, no es posible.",
    "No deberías confiar en lo que los demás dicen sobre mí, saben que soy diferente."
]

# Funciones del juego
def investigar():
    pista = random.choice(resultados_investigacion)
    messagebox.showinfo("Investigación", f"Pista encontrada: {pista}")

def interrogar():
    interrogar_window = tk.Toplevel(root)
    interrogar_window.title("Interrogar a un personaje")

    def seleccionar_personaje():
        eleccion = personaje_var.get()
        personaje = personajes[int(eleccion)]
        respuesta = random.choice(respuestas_culpable) if personaje == culpable else random.choice(respuestas_inocente)
        messagebox.showinfo("Respuesta", f"{personaje['nombre']} responde: {respuesta}")

    personaje_var = tk.StringVar(value="0")
    for i, personaje in enumerate(personajes):
        rb = tk.Radiobutton(interrogar_window, text=f"{personaje['nombre']} ({personaje['profesion']})", variable=personaje_var, value=i)
        rb.pack(anchor='w')

    tk.Button(interrogar_window, text="Interrogar", command=seleccionar_personaje).pack()

def acusar():
    acusar_window = tk.Toplevel(root)
    acusar_window.title("Acusar al culpable")

    def seleccionar_acusado():
        eleccion = personaje_var.get()
        acusado = personajes[int(eleccion)]
        if acusado == culpable:
            messagebox.showinfo("Acusación", f"¡Felicidades! Has resuelto el caso. El culpable era {acusado['nombre']} con un(a) {arma_seleccionada} en {locacion_seleccionada}.")
        else:
            messagebox.showwarning("Acusación fallida", f"Lo siento, {acusado['nombre']} no es el culpable.")

    personaje_var = tk.StringVar(value="0")
    for i, personaje in enumerate(personajes):
        rb = tk.Radiobutton(acusar_window, text=f"{personaje['nombre']} ({personaje['profesion']})", variable=personaje_var, value=i)
        rb.pack(anchor='w')

    tk.Button(acusar_window, text="Acusar", command=seleccionar_acusado).pack()

# Interfaz gráfica
root = tk.Tk()
root.title("Juego de Clue - Cibercrimen en Neo-Capital City")

# Menú principal
tk.Label(root, text="Bienvenido al juego de Clue - Cibercrimen en Neo-Capital City", font=("Arial", 14)).pack(pady=10)
tk.Label(root, text=f"El crimen ocurrió en: {locacion_seleccionada}\n{locaciones[locacion_seleccionada]}", wraplength=400).pack(pady=5)

# Botones para las opciones del menú
tk.Button(root, text="Investigar la locación", command=investigar, width=30).pack(pady=5)
tk.Button(root, text="Interrogar a un personaje", command=interrogar, width=30).pack(pady=5)
tk.Button(root, text="Acusar al culpable", command=acusar, width=30).pack(pady=5)
tk.Button(root, text="Salir", command=root.quit, width=30).pack(pady=5)

# Iniciar la interfaz
root.mainloop()
