import cv2
import mediapipe as mp

# Configurando OpenCV e Mediapipe
webcam = cv2.VideoCapture(0)
solucao = mp.solutions.face_detection
reconhecer = solucao.FaceDetection()
desenho = mp.solutions.drawing_utils

while True:
    # Verificando se a camêra está funcionando
    verificar, imagem = webcam.read()
    if not verificar:
        break
    
    # Reconhecendo rostos na camêra
    lista_de_rostos = reconhecer.process(imagem)

    # Desenhando na imagem da camêra
    if lista_de_rostos.detections:
        for rosto in lista_de_rostos.detections:
            desenho.draw_detection(imagem, rosto)
    cv2.imshow('Teste de camêra', imagem)

    # Código para fechar a camêra no ESC
    if cv2.waitKey(5) == 27:
        break

webcam.release()
cv2.destroyAllWindows()