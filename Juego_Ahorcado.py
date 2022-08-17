from random import choice

palabras = ['panadero', 'dinosaurio', 'helipuerto', 'tiburon']
letras_correctas = []
letras_incorrectas = []
intentos = 6
aciertos = 0
juego_terminado = False


def elegir_palbra(lista_palabras):
    palabra_elegida = choice(lista_palabras)
    letras_unicas = len(set(palabra_elegida))

    return palabra_elegida, letras_unicas


def pedir_letra():
    letra_elegida = ''
    es_valida = False
    abecedario = 'abcdefghijklmnñopqrstuvwxyz'

    while not es_valida:
        letra_elegida = input("Elige una letra: ")
        if letra_elegida in abecedario and len(letra_elegida) == 1:
            es_valida = True
        else:
            print("No has elegido una letra correcta")

    return letra_elegida


def mostrar_nuevo_tablero(palabra_elegida):

    lista_oculta = []

    for l in palabra_elegida:
        if l in letras_correctas:
            lista_oculta.append(l)
        else:
            lista_oculta.append('-')

    print(' '.join(lista_oculta))
