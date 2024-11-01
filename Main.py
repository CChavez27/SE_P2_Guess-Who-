import json
import tkinter as tk
from tkinter import messagebox

# Base de datos de componentes electrónicos en formato JSON
componentes_iniciales = [
    {
        "nombre": "Resistencia",
        "es_pasivo": True,
        "es_activo": False,
        "tiene_polaridad": False,
        "es_semiconductor": False,
        "tiene_tres_pines": False,
        "puede_amplificar_senales": False,
        "puede_almacenar_energia": False,
        "es_dispositivo_proteccion": False,
        "es_microcontrolador": False,
        "es_regulador_voltaje": False,
    },
    # (agrega los otros componentes aquí)
]

# Guardar los componentes en un archivo JSON si no existe
try:
    with open('componentes.json', 'r') as f:
        pass  # Si el archivo ya existe, no hacemos nada
except FileNotFoundError:
    with open('componentes.json', 'w') as f:
        json.dump(componentes_iniciales, f)

# Cargar componentes desde el archivo JSON
def cargar_componentes():
    with open('componentes.json', 'r') as f:
        return json.load(f)

# Clase principal para el juego
class AdivinaQuien:
    def __init__(self, root):
        self.root = root
        self.root.title("Adivina Quién - Componentes Electrónicos")
        
        self.componentes = cargar_componentes()
        self.opciones = self.componentes.copy()
        self.indice = 0
        
        self.pregunta_label = tk.Label(root, text="")
        self.pregunta_label.pack()
        
        self.respuesta_entry = tk.Entry(root)
        self.respuesta_entry.pack()
        
        self.submit_button = tk.Button(root, text="Enviar respuesta", command=self.process_response)
        self.submit_button.pack()
        
        self.next_button = tk.Button(root, text="Siguiente pregunta", command=self.next_question)
        self.next_button.pack()
        
        self.resultado_label = tk.Label(root, text="")
        self.resultado_label.pack()

        self.iniciar_juego()

    def iniciar_juego(self):
        self.indice = 0
        self.opciones = cargar_componentes()
        self.next_question()

    def next_question(self):
        if self.indice < len(preguntas):
            self.pregunta_label.config(text=preguntas[self.indice]['mensaje'])
            self.respuesta_entry.delete(0, tk.END)
        else:
            self.adivinar_componente()

    def process_response(self):
        respuesta = self.respuesta_entry.get().strip().lower()
        if respuesta not in ['s', 'n']:
            messagebox.showwarning("Advertencia", "Por favor, responde con 's' o 'n'.")
            return

        # Filtrar las opciones basadas en la respuesta
        atributo = preguntas[self.indice]['atributo']
        self.opciones = [comp for comp in self.opciones if comp[atributo] == (respuesta == 's')]
        
        self.indice += 1
        self.next_question()

    def adivinar_componente(self):
        if len(self.opciones) == 1:
            nombre = self.opciones[0]['nombre']
            self.resultado_label.config(text=f"Creo que tu componente es: {nombre}")
        else:
            self.resultado_label.config(text="No he podido adivinar el componente.")
            self.aprender_componente()
        self.pregunta_label.config(text="")
        self.respuesta_entry.config(state='disabled')
        self.submit_button.config(state='disabled')

    def aprender_componente(self):
        # Aquí puedes agregar la lógica para aprender un nuevo componente
        messagebox.showinfo("Aprender Componente", "Vamos a aprender un nuevo componente.")
        # Aquí podrías implementar una ventana emergente o algo similar para ingresar un nuevo componente.

# Preguntas a hacer al usuario
preguntas = [
    {"atributo": "es_pasivo", "mensaje": "¿Es un componente pasivo? (s/n): "},
    {"atributo": "es_activo", "mensaje": "¿Es un componente activo? (s/n): "},
    {"atributo": "tiene_polaridad", "mensaje": "¿El componente tiene polaridad? (s/n): "},
    {"atributo": "es_semiconductor", "mensaje": "¿Es un semiconductor? (s/n): "},
    {"atributo": "tiene_tres_pines", "mensaje": "¿Tiene tres pines? (s/n): "},
    {"atributo": "puede_amplificar_senales", "mensaje": "¿Puede amplificar señales? (s/n): "},
    {"atributo": "puede_almacenar_energia", "mensaje": "¿Puede almacenar energía? (s/n): "},
    {"atributo": "es_dispositivo_proteccion", "mensaje": "¿Es un dispositivo de protección? (s/n): "},
    {"atributo": "es_microcontrolador", "mensaje": "¿Es un microcontrolador? (s/n): "},
    {"atributo": "es_regulador_voltaje", "mensaje": "¿Es un regulador de voltaje? (s/n): "},
]

# Función principal
if __name__ == "__main__":
    root = tk.Tk()
    app = AdivinaQuien(root)
    root.mainloop()
