import cv2
import time
import math

#carregando o vídeo
video = cv2.VideoCapture("./bb3.mp4")

# Carregando o ratreador
tracker = cv2.TrackerCSRT_create()

# Lendo o primeiro quadro do vídeo
ret, frame = video.read()

# selecionando a caixa delimitadora
bbox = cv2.selectROI("Rastreando",frame,False)

#inicializando o rastreador
tracker.init(frame,bbox)

#criar função para desenhar a caixa delimitadora na bola
def DrawBox(img,bbox):
    x,y,w,h = int(bbox [0]),int(bbox [1]),int(bbox[2]),int(bbox[3])
    cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,43),3,1)
    cv2.putText(img,"rastreando",(75,140),cv2.FONT_ITALIC,0.7,(67,32,0),2)


#criar função para rastrear a bola
def trackingBall():
    pass

while True:
    #lendo o quadro do vídeo
    check, frame = video.read()

    success,bbox = tracker.update(frame)
    if success:
        DrawBox(frame,bbox)
        
    #exibindo o quando do vídeo
    cv2.imshow("Resultado",frame)

    #evitar que a janela feche em seguida
    key = cv2.waitKey(25)

    if key == 32:
        print("interrompido")
        break

video.release()
cv2.destroyAllWindows()
