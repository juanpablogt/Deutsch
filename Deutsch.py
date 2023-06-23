import random

vocabulario_semana_1 = {
    "Guten Morgen": "Buenos dias",
    "Hallo": "Hola",
    "Wie geht es dir?": "¿Como estas?",
    "Ich heiße": "Me llamo",
    "Woher kommst du?": "¿De donde eres?"
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

pistas_semana_1 = {
    "Guten Morgen": ["La primera letra es 'G'", "La última letra es 'n'", "Contiene la letra 'e'"],
    "Hallo": ["La primera letra es 'H'", "La segunda letra es 'a'", "Contiene la letra 'o'"],
    "Wie geht es dir?": ["La primera letra es 'W'", "La segunda letra es 'i'", "Contiene la letra 's'"],
    "Ich heiße": ["La primera letra es 'I'", "La segunda letra es 'c'", "Contiene la letra 'e'"],
    "Woher kommst du?": ["La primera letra es 'W'", "La segunda letra es 'o'", "Contiene la letra 'h'"]
}

pistas_semana_2 = {
    "Familie": ["La primera letra es 'F'", "La segunda letra es 'a'", "Contiene la letra 'i'"],
    "Mutter": ["La primera letra es 'M'", "La segunda letra es 'u'", "Contiene la letra 'e'"],
    "Vater": ["La primera letra es 'V'", "La segunda letra es 'a'", "Contiene la letra 't'"],
    "Geschwister": ["La primera letra es 'G'", "La segunda letra es 'e'", "Contiene la letra 'w'"],
    "Sohn": ["La primera letra es 'S'", "La segunda letra es 'o'", "Contiene la letra 'h'"],
    "Tochter": ["La primera letra es 'T'", "La segunda letra es 'o'", "Contiene la letra 'c'"]
}

# ... Continúa creando diccionarios de pistas para cada semana

def jugar_juego_vocabulario(vocabulario, pistas, num_intentos):
    palabras = list(vocabulario.keys())
    jugadores = []
    puntajes = {}

    print("\n\n----------¡vocabulario en alemán!----------")
    print("\n Nota: Debes ingresar la traducción correcta en español de la palabra en alemán.")

    # Pedir nombres de los jugadores
    num_jugadores = int(input("->Ingrese el número de jugadores: "))
    for i in range(num_jugadores):
        nombre = input(f"->Ingrese el nombre del jugador {i+1}: ")
        jugadores.append(nombre)
        puntajes[nombre] = 0

    while len(palabras) > 0:
        for jugador in jugadores:
            palabra_alemana = random.choice(palabras)
            palabra_espanol = vocabulario[palabra_alemana]
            pistas_palabra = pistas[palabra_alemana]

            print("\n----->Tu Turno", jugador)
            print("---------------------------")
            print("Pista 1:", pistas_palabra[0])

            intentos_restantes = num_intentos
            respuesta_correcta = False

            while intentos_restantes > 0 and not respuesta_correcta:
                respuesta_usuario = input("\n---->Traducción de '" + palabra_alemana + "': ").lower()

                if respuesta_usuario == palabra_espanol.lower():
                    print("¡Correcto!")
                    puntajes[jugador] += 1
                    palabras.remove(palabra_alemana)
                    respuesta_correcta = True
                else:
                    intentos_restantes -= 1
                    if intentos_restantes > 0:
                        print("Incorrecto. Inténtalo nuevamente. Intentos restantes:", intentos_restantes)

            if not respuesta_correcta:
                print("Respuesta incorrecta. La respuesta correcta era:", palabra_espanol)

        # Mostrar puntuaciones parciales
        print("\nPuntuaciones parciales:")
        for jugador in jugadores:
            print(jugador + ":", puntajes[jugador])

    print("\n::::::::::Juego terminado::::::::::")
    print("\n---->Puntajes finales:")
    for jugador in jugadores:
        print(jugador + ":", puntajes[jugador], "/", len(vocabulario))

def obtener_pistas(palabra, pistas_semana):
    pistas = pistas_semana[palabra]
    return pistas

# Inicio del programa
def menu():
    print("\n-----------¡Bienvenido al juego de vocabulario en alemán!-----------")
    print("\nSeleccione una opción:")
    print("1. Woche 1")
    print("2. Woche 2")
    print("3. Salir")
    opcion = int(input("\nIngrese una opción: "))
    return opcion

opcion = menu()
num_intentos = int(input("->Ingrese el número de intentos por palabra: "))  # Pedir número de intentos una vez al inicio

while opcion != 3:
    if opcion == 1:
        jugar_juego_vocabulario(vocabulario_semana_1, pistas_semana_1, num_intentos)
    elif opcion == 2:
        jugar_juego_vocabulario(vocabulario_semana_2, pistas_semana_2, num_intentos)
    opcion = menu()

print("¡Hasta luego!")

# Fin del programa