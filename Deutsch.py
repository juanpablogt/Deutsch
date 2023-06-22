import random

vocabulario_semana_1 = {
    "Guten Morgen": "Buenos días",
    "Hallo": "Hola",
    "Wie geht es dir?": "¿Cómo estás?",
    "Ich heiße...": "Me llamo...",
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

def jugar_juego_vocabulario(diccionario_vocabulario):
    """
    Esta función recibe un diccionario de vocabulario y genera un juego de preguntas y respuestas
    para que el usuario pueda practicar.
    """
    # Generamos una lista con todas las palabras del diccionario
    palabras = list(diccionario_vocabulario.keys())
    # Mezclamos la lista de palabras
    random.shuffle(palabras)
    # Iteramos sobre la lista de palabras
    for palabra in palabras:
        # Mostramos la palabra en alemán
        print(palabra)
        # Leemos la respuesta del usuario
        respuesta = input("¿Qué significa esta palabra? ")
        # Obtenemos la respuesta correcta del diccionario
        respuesta_correcta = diccionario_vocabulario[palabra]
        # Comparamos la respuesta del usuario con la respuesta correcta
        if respuesta == respuesta_correcta:
            # Si la respuesta es correcta, mostramos un mensaje de felicitación
            print("¡Muy bien!")
        else:
            # Si la respuesta es incorrecta, mostramos la respuesta correcta
            print("Estas equivocado La respuesta correcta es:", respuesta_correcta)

# Esta es la función principal del programa
def main():

    # Creamos un diccionario que contiene los diccionarios de vocabulario de cada semana
    vocabulario = {
        1: vocabulario_semana_1,
        2: vocabulario_semana_2
    }

    # Leemos el número de semana que quiere practicar el usuario
    semana = int(input("¿Qué semana quieres practicar? "))
    # Obtenemos el diccionario de vocabulario de la semana que quiere practicar el usuario
    diccionario_vocabulario = vocabulario[semana]
    # Llamamos a la función que genera el juego de preguntas y respuestas
    jugar_juego_vocabulario(diccionario_vocabulario)

# Llamamos a la función principal
main()
