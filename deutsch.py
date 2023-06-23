import random
import tkinter as tk

vocabulario_semana_1 = {
    "Guten Morgen": "Buenos días",
    "Hallo": "Hola",
    "Wie geht es dir?": "¿Cómo estás?",
    "Ich heiße...": "Me llamo...",
    "Woher kommst du?": "¿De dónde eres?"
}

# ... Define los diccionarios de vocabulario para cada semana

def jugar_juego_vocabulario(vocabulario):
    palabras = list(vocabulario.keys())
    jugadores = []
    puntajes = {}

    # Crear ventana
    ventana = tk.Tk()
    ventana.title("Juego de Vocabulario Alemán")
    
    # Crear elementos de la interfaz
    etiqueta_turno = tk.Label(ventana, text="Turno de:")
    etiqueta_palabra = tk.Label(ventana, text="Palabra:")
    etiqueta_pista = tk.Label(ventana, text="Pista:")
    entrada_respuesta = tk.Entry(ventana)
    boton_enviar = tk.Button(ventana, text="Enviar", command=lambda: verificar_respuesta(palabras, jugadores, puntajes, entrada_respuesta))

    # Posicionar elementos en la ventana
    etiqueta_turno.grid(row=0, column=0)
    etiqueta_palabra.grid(row=1, column=0)
    etiqueta_pista.grid(row=2, column=0)
    entrada_respuesta.grid(row=3, column=0)
    boton_enviar.grid(row=4, column=0)

    def iniciar_juego():
        print("¡Bienvenido al juego de vocabulario en alemán!")
        print("Ingresa la traducción correcta en español de la palabra en alemán.")
        print("Tienes tres pistas para cada palabra.")

        # Pedir nombres de los jugadores
        num_jugadores = int(input("Ingrese el número de jugadores: "))
        for i in range(num_jugadores):
            nombre = input(f"Ingrese el nombre del jugador {i+1}: ")
            jugadores.append(nombre)
            puntajes[nombre] = 0

        siguiente_turno()

    def siguiente_turno():
        jugador_actual = jugadores[0]
        palabra_alemana = random.choice(palabras)
        palabra_espanol = vocabulario[palabra_alemana]
        pistas = obtener_pistas(palabra_alemana)

        # Actualizar elementos de la interfaz
        etiqueta_turno.configure(text="Turno de: " + jugador_actual)
        etiqueta_palabra.configure(text="Palabra: " + palabra_alemana)
        etiqueta_pista.configure(text="Pista: " + pistas[0])
        entrada_respuesta.delete(0, tk.END)

    def verificar_respuesta(palabras, jugadores, puntajes, entrada_respuesta):
        respuesta_usuario = entrada_respuesta.get().lower()
        jugador_actual = jugadores[0]
        palabra_alemana = etiqueta_palabra.cget("text").split(": ")[1]

        if respuesta_usuario == vocabulario[palabra_alemana]:
            print("¡Correcto!")
            puntajes[jugador_actual]
            palabras.remove(palabra_alemana)
        else:
            print("Incorrecto. Inténtalo nuevamente en tu próximo turno.")

        # Actualizar elementos de la interfaz
        entrada_respuesta.delete(0, tk.END)
        jugadores.append(jugadores.pop(0))
        siguiente_turno()

    def obtener_pistas(palabra_alemana):
        pistas = []
        for i in range(3):
            pista = ""
            for j in range(i+1):
                pista += palabra_alemana[j]
            pistas.append(pista)
        return pistas
    
    iniciar_juego()
    ventana.mainloop()

jugar_juego_vocabulario(vocabulario_semana_1)
