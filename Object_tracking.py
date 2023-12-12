import cv2
import time
import math

p1 = 530
p2 = 300

xs = []
ys = []

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
    cv2.putText(img,"rastreando",(75,140),cv2.FONT_ITALIC,0.7,(67,32,255),2)


#criar função para rastrear a bola
def trackingBall(img, bbox):
    pass
    #Roberta
    #DESENHAR CIRCULO NO CENTRO DA BOLA
    x,y,w,h = int(bbox [0]),int(bbox [1]),int(bbox[2]),int(bbox[3])
    c1 = x + int(w/2)
    c2 = y + int(h/2)
    cv2.circle(img, (c1,c2),2,(0,0,0),3)

    #Marcos
    #DESENHAR CIRCULO NO CENTRO DA CESTA
    cv2.circle(img, (p1,p2),2,(74,130,200),3)
    #André
    #CALCULAR DISTANCIA ENTRE A BOLA E A CESTA
    # D = √ (x2-x1)² + (y2 - y1)²
    
    distance = math.sqrt((c1-p1)**2 + (c2-p2)**2)
    #VERIFICAR A DISTANCIA ENTRE A CESTA E BOLA E EXIBIR UM TEXTO EM CASO DE COLISÃO
    if distance <= 20:
        cv2.putText(img, "CESTA", (75,175),cv2.FONT_ITALIC,0.7,(67,32,255),2)


    #Bruna
    #ARMAZENAR AS COORDENADAS DA BOLA
    xs.append(c1)
    ys.append(c2)

    #EXIBIR A TRAGETÓRIA DA BOLA NA TELA
    for i in range(len(xs)):
        cv2.circle(img, (xs[i], ys[i]), 2, (0,0,0), 2)

while True:
    #lendo o quadro do vídeo
    check, frame = video.read()

    success,bbox = tracker.update(frame)
    if success:
        DrawBox(frame,bbox)
    else:
        cv2.putText(frame,"Errou",(75,90),cv2.FONT_HERSHEY_SIMPLEX,0.7,(0,0,255),2)

    #CHAMAR FUNÇÃO AQUI
    trackingBall(frame, bbox)
        
    #exibindo o quando do vídeo
    cv2.imshow("Resultado",frame)

    #evitar que a janela feche em seguida
    key = cv2.waitKey(25)

    if key == 32:
        print("interrompido")
        break

video.release()
cv2.destroyAllWindows()



#instalações
#pip install opencv-python
#pip install opencv-contrib-python  
