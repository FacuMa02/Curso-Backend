import random

palabras = ['gato', 'perro', 'elefante', 'jirafa',
            'rinoceronte', 'leon', 'tigre', 'cebra', 'mono']


def elegir_palabra(lista_palabras):
    palabra = random.choice(lista_palabras)
    return palabra


def jugar(palabra):
    longitud_palabra = len(palabra)
    intentos = 6
    letras_adivinadas = []
    guiones = '-' * longitud_palabra
    juego_terminado = False

    print('Bienvenido al juego del Ahorcado. Adivina la palabra:')
    print(guiones)

    while not juego_terminado:
        letra = input('Ingresa una letra: ')

        if letra in palabra:
            letras_adivinadas.append(letra)
            print('Adivinaste una letra.')
        else:
            intentos -= 1
            print('Incorrecto. Te quedan', intentos, 'intentos.')

        indices_letra = [i for i, x in enumerate(palabra) if x == letra]
        for i in indices_letra:
            guiones = guiones[:i] + letra + guiones[i+1:]

        print(guiones)

        if intentos == 0:
            print('Perdiste. La palabra era', palabra)
            juego_terminado = True

        if guiones == palabra:
            print('¡Ganaste!')
            juego_terminado = True


palabra = elegir_palabra(palabras)
jugar(palabra)
