
import cv2
import numpy as np
from matplotlib import pyplot as plt

def mostrar_menu(opciones):
    print('Imagen de Lena')
    print('Seleccione una opción:')
    for clave in sorted(opciones):
        print(f' {clave}) {opciones[clave][0]}')


def leer_opcion(opciones):
    while (a := input('Opción: ')) not in opciones:
        print('Opción incorrecta, vuelva a intentarlo.')
    return a


def ejecutar_opcion(opcion, opciones):
    opciones[opcion][1]()


def generar_menu(opciones, opcion_salida):
    opcion = None
    while opcion != opcion_salida:
        mostrar_menu(opciones)
        opcion = leer_opcion(opciones)
        ejecutar_opcion(opcion, opciones)
        print()


def menu_principal():
    opciones = {
        '1': ('Opción 1 : Escala de grises', accion1),
        '2': ('Opción 2 : Conversión binaria ', accion2),
        '3': ('Opción 3  : Histograma', accion3),
        '4': ('Opción 4  : Aumentar contraste', accion4),
        '5': ('Opción 5  : Histograma convertido ', accion5),
        '6': ('Salir', salir)
    }

    generar_menu(opciones, '6')


def accion1():

    #cargar imagen a color de parchis
    img_color = cv2.imread('leena.jpg')   

    #Transformacion a gris 
    img_gray = cv2.cvtColor(img_color, cv2.COLOR_BGR2GRAY)

    #Mostrar imagenes por pantalla
    cv2.imshow('Color', img_color)
    cv2.imshow('Gris', img_gray)

    #Cerrar ventanas
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def accion2():
    # read the image file
    img = cv2.imread('leena.jpg', 2)
    
    ret, bw_img = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
    
    cv2.imshow("Binary", bw_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def accion3():

    #cargar imagen a color de parchis
    img_color = cv2.imread('leena.jpg')   

    #Transformacion a gris 
    img_gray = cv2.cvtColor(img_color, cv2.COLOR_BGR2GRAY)

    #Mostrar imagenes por pantalla
    cv2.imshow('Color', img_color)
    cv2.imshow('leena.jpg', img_gray)
    
    #calcular histograma para grises

    hist = cv2.calcHist([img_gray], [0], None, [256], [0, 256])
    plt.plot(hist, color='gray' )

    plt.xlabel('intensidad de iluminacion')
    plt.ylabel('cantidad de pixeles')
    plt.show()

    #Cerrar ventanas
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
def accion4():
    
    #cargar imagen a color de parchis
    img_color = cv2.imread('leena.jpg')   

    #Transformacion a gris 
    img_gray = cv2.cvtColor(img_color, cv2.COLOR_BGR2GRAY)

    alpha = 0.6# Contrast control (1.0-3.0)
    beta = 0# Brightness control (0-100)

    adjusted = cv2.convertScaleAbs(img_gray, alpha=alpha, beta=beta)
    
    #Mostrar imagenes por pantalla
    cv2.imshow('original', img_gray)
    cv2.imshow('adjusted', adjusted)
    #Cerrar ventanas
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def accion5():
    
    #cargar imagen a color de lena
    img_color = cv2.imread('leena.jpg')   

    #Transformacion a gris 
    img_gray = cv2.cvtColor(img_color, cv2.COLOR_BGR2GRAY)

    alpha = 0.6# Contrast control (1.0-3.0)
    beta = 0# Brightness control (0-100)

    adjusted = cv2.convertScaleAbs(img_gray, alpha=alpha, beta=beta)
    
    #Mostrar imagenes por pantalla
    cv2.imshow('original', img_gray)
    cv2.imshow('adjusted', adjusted)
    
    hist = cv2.calcHist([adjusted], [0], None, [256], [0, 256])
    plt.plot(hist, color='gray' )

    plt.xlabel('intensidad de iluminacion')
    plt.ylabel('cantidad de pixeles')
    plt.show()

    #Cerrar ventanas
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def salir():
    print('Saliendo')

if __name__ == '__main__':
    menu_principal()