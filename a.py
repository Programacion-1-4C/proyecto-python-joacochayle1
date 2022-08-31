from Funciones_ahorcado import pistas_palabras , elegir_palbra, pedir_letra, mostrar_nuevo_tablero, chequear_letra
palabras = ['panadero', 'dinosaurio', 'helipuerto', 'tiburon','cars','meteoro']
letras_correctas = []
letras_incorrectas = []
intentos = 10
aciertos = 0
juego_terminado = False



palabra, letras_unicas = elegir_palbra(palabras)

while not juego_terminado:
    print('\n' + '*' * 20 + '\n')
    pistas_palabras(palabra)
    mostrar_nuevo_tablero(palabra)
    print('\n')
    print('Letras incorrectas: ' + '-'.join(letras_incorrectas))
    print(f'Vidas: {intentos}')
    print(letras_correctas)
    print('\n' + '*' * 20 + '\n')
    letra = pedir_letra()

    intentos, terminado, aciertos = chequear_letra(letra,palabra,intentos,aciertos)

    juego_terminado = terminado
