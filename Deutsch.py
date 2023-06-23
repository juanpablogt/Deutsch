import random

vocabulario_semana_1 = {
    "Guten Morgen": "Buenos dias",
    "Hallo": "Hola",
    "Wie geht es dir?": "¿Como estas?",
    "Ich heiße...": "Me llamo",
    "Woher kommst du?": "¿De dónde eres?"
}

vocabulario_semana_2 = {
    "Familie": "familia",
    "Mutter": "madre",
    "Vater": "padre",
    "Geschwister": "hermanos",
    "Sohn": "hijo",
    "Tochter": "hija"
}

# ... Continúa creando diccionarios de vocabulario para cada semana

def jugar_juego_vocabulario(vocabulario):
    palabras = list(vocabulario.keys())
    jugadores = []
    puntajes = {}

    print("¡Bienvenido al juego de vocabulario en alemán!")
    print("Ingresa la traducción correcta en español de la palabra en alemán.")
    print("Tienes tres pistas para cada palabra.")

    # Pedir nombres de los jugadores
    num_jugadores = int(input("Ingrese el número de jugadores: "))
    for i in range(num_jugadores):
        nombre = input(f"Ingrese el nombre del jugador {i+1}: ")
        jugadores.append(nombre)
        puntajes[nombre] = 0

    while len(palabras) > 0:
        for jugador in jugadores:
            palabra_alemana = random.choice(palabras)
            palabra_espanol = vocabulario[palabra_alemana]
            pistas = obtener_pistas(palabra_alemana)

            print("\nTurno de", jugador)
            print("Nueva palabra:")
            print("Pista 1:", pistas[0])

            respuesta_usuario = input("Traducción de '" + palabra_alemana + "': ").lower()

            if respuesta_usuario.lower() == palabra_espanol.lower() or respuesta_usuario == palabra_espanol:
                print("¡Correcto!")
                puntajes[jugador] += 1
                palabras.remove(palabra_alemana)
            else:
                print("Incorrecto. Inténtalo nuevamente en tu próximo turno.")

        # Mostrar puntuaciones parciales
        print("\nPuntuaciones parciales:")
        for jugador in jugadores:
            print(jugador + ":", puntajes[jugador])

    print("\n¡Juego terminado!")
    print("Puntajes finales:")
    for jugador in jugadores:
        print(jugador + ":", puntajes[jugador], "/", len(vocabulario))

def obtener_pistas(palabra):
    pistas = []
    for i in range(3):
        letra = random.choice(palabra)
        while letra in pistas:
            letra = random.choice(palabra)
        pistas.append(letra)
    return pistas

# Inicio del programa

print("¡Bienvenido al curso de alemán!")

while True:
    print("\nSeleccione una opción:")
    print("1. Jugar juego de vocabulario semana 1")
    print("2. Jugar juego de vocabulario semana 2")
    print("3. Jugar juego de vocabulario semana 3")
    print("4. Salir")

    opcion = int(input("Opción: "))

    if opcion == 1:
        jugar_juego_vocabulario(vocabulario_semana_1)
    elif opcion == 2:
        jugar_juego_vocabulario(vocabulario_semana_2)
    elif opcion == 3:
        break
    else:
        print("Opción inválida. Inténtalo nuevamente.")

print("¡Hasta luego!")

# Fin del programa
