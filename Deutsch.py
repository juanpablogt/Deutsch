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

class JuegoVocabularioCLI:
    def __init__(self, vocabulario):
        self.vocabulario = vocabulario
        self.palabras = list(self.vocabulario.keys())
        random.shuffle(self.palabras)
        self.palabra_actual = 0
        self.puntaje = 0

    def jugar(self):
        print("¡Bienvenido al juego de vocabulario en alemán!")
        print("Ingresa la traducción correcta en español de la palabra en alemán.")
        print("Tienes tres oportunidades para cada palabra.")

        for palabra in self.palabras:
            print("\nNueva palabra:")
            print(palabra)

            respuesta_correcta = self.vocabulario[palabra]
            oportunidades = 3

            while oportunidades > 0:
                respuesta_usuario = input("Traducción: ").lower()

                if respuesta_usuario == respuesta_correcta.lower():
                    print("¡Respuesta correcta!")
                    self.puntaje += 1
                    break
                else:
                    oportunidades -= 1
                    if oportunidades > 0:
                        print("Respuesta incorrecta. Inténtalo nuevamente. Oportunidades restantes:", oportunidades)

            if oportunidades == 0:
                print("Respuesta incorrecta. La respuesta correcta es:", respuesta_correcta)

        print("\n¡Juego terminado!")
        print("Puntaje final:", self.puntaje, "/", len(self.vocabulario))

def main():
    vocabulario = {
        1: vocabulario_semana_1,
        2: vocabulario_semana_2
    }

    semana = int(input("¿Qué semana quieres practicar? "))
    diccionario_vocabulario = vocabulario[semana]

    juego = JuegoVocabularioCLI(diccionario_vocabulario)
    juego.jugar()

if __name__ == "__main__":
    main()

