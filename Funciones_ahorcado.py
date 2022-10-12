from random import choice




def elegir_palbra(lista_palabras):
    palabra_elegida = choice(lista_palabras)
    letras_unicas = len(set(palabra_elegida))

    return palabra_elegida, letras_unicas

def pistas_palabras(palabra):
    if palabra== "panadero":
        print('La palabra que estas buscando tiene que ver con alguien que cocina cosas para que desayunes')
    if palabra== "dinosaurio":
        print("Estamos hablando de un tipo de 'animal' que vivia hace muchos años en la tierra")
    if palabra== "helipuerto":
        print("Lugar donde se estacionan vehiculos aéreos con aspas ")
    if palabra== "tiburon":
        print("Animal marino muy temido")
    if palabra== "cars":
        print("Película de Disney relacionada a los autos ")
    if palabra== "meteoro":
        print("película de carreras con autos con propulsores, el nombre tiene que ver con algo que mato a los dinosaurios")
    if palabra=="biologia":
        print("Materia del colegio que se encarga de estudiar la vida")
    return palabra

def pedir_letra(letras_correctas):
    letra_elegida = ''
    es_valida = False
    abecedario = 'abcdefghijklmnñopqrstuvwxyz'

    while not es_valida:
        letra_elegida = input("Elige una letra: ")
        if letra_elegida in abecedario and len(letra_elegida) == 1:
            es_valida = True
            if letra_elegida in letras_correctas:
                print("Ya has usado esta letra")
                es_valida = False
        else:
            print("No has elegido una letra correcta")

    return letra_elegida



def mostrar_nuevo_tablero(palabra_elegida, letras_correctas):

    lista_oculta = []

    for l in palabra_elegida:
        if l in letras_correctas:
            lista_oculta.append(l)
        else:
            lista_oculta.append('-')

    print(' '.join(lista_oculta))

def chequear_letra(letra_elegida, palabra_oculta, vidas, coincidencias, letras_correctas, letras_incorrectas):
    if letra_elegida in palabra_oculta:
        letras_correctas.append(letra_elegida)
        coincidencias += 1
    else:
        letras_incorrectas.append(letra_elegida)
        vidas -= 1
    return vidas, coincidencias


def perder(palabra):
    print("Te has quedado sin vidas")
    print("La palabra oculta era " + palabra)

    return True
def ganar(palabra_descubierta, letras_correctas):
    mostrar_nuevo_tablero(palabra_descubierta, letras_correctas)
    print("Felicitaciones, has encontrado la palabra!!!")

    return True
