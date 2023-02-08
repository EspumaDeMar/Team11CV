import cv2
import numpy as np

img= cv2.imread('50soles.jpg')
imghsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
pixeles_totales=img.size


"""" CONTROL CELESTE / 100 SOLES """
celestebajo=np.array([90,50,50],np.uint8)
celestealto=np.array([107,255,255],np.uint8)
mascaraceleste=cv2.inRange(imghsv,celestebajo,celestealto)
pixeles_encendidos_celeste=cv2.countNonZero(mascaraceleste)

"""" CONTROL MAGENTE / 50 SOLES """
magentabajo=np.array([0,50,50],np.uint8)
magentaalto=np.array([10,150,255],np.uint8)
mascaramagenta=cv2.inRange(imghsv,magentabajo,magentaalto)
pixeles_encendidos_magenta=cv2.countNonZero(mascaramagenta)

"""" CONTROL AMARILLO / 20 SOLES """
amarillobajo=np.array([10,50,50],np.uint8)
amarilloalto=np.array([20,255,255],np.uint8)
mascaraamarilla=cv2.inRange(imghsv,amarillobajo,amarilloalto)
pixeles_encendidos_amarilla=cv2.countNonZero(mascaraamarilla)


if pixeles_encendidos_amarilla>pixeles_encendidos_celeste and pixeles_encendidos_amarilla>pixeles_encendidos_magenta:
    print("billete de 20 soles")



if pixeles_encendidos_magenta>pixeles_encendidos_celeste and pixeles_encendidos_magenta>pixeles_encendidos_amarilla:
    print("billete de 50 soles")


if pixeles_encendidos_celeste>pixeles_encendidos_amarilla and pixeles_encendidos_celeste>pixeles_encendidos_magenta:
    print("billete de 100 soles")


cv2.imshow('imagen entrada',img)
cv2.imshow('imagen hsv',imghsv)
cv2.imshow('Mascara celeste', mascaraceleste)
cv2.imshow('Mascara amarilla', mascaraamarilla)
cv2.imshow('Mascara magenta', mascaramagenta)

cv2.waitKey(0)
cv2.destroyAllWindows()