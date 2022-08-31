from Funciones_ahorcado import pistas_palabras, elegir_palbra, pedir_letra, mostrar_nuevo_tablero, chequear_letra, ganar,perder

palabras = ['panadero', 'dinosaurio', 'helipuerto', 'tiburon', 'cars', 'meteoro', 'biologia']
letras_correctas = []
letras_incorrectas = []
intentos = 10
aciertos = 0
juego_terminado = False


palabra, letras_unicas = elegir_palbra(palabras)



while not juego_terminado:
    print('\n' + '*' * 20 + '\n')
    pistas_palabras(palabra)
    mostrar_nuevo_tablero(palabra, letras_correctas)
    print('\n')
    print('Letras incorrectas: ' + '-'.join(letras_incorrectas))
    print(f'Vidas: {intentos}')
    print('\n' + '*' * 20 + '\n')
    letra = pedir_letra(letras_correctas)

    intentos, aciertos = chequear_letra(letra, palabra, intentos, aciertos, letras_correctas, letras_incorrectas)
    if intentos==0:
        juego_terminado=perder(palabra)
    elif aciertos==letras_unicas:
        juego_terminado=ganar(letras_correctas, palabra)


