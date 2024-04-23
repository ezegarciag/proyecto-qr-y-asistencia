import cv2
from pyzbar.pyzbar import decode
import time
import threading
import pygame

class QRDetector:
    def __init__(self, callback):
        self.callback = callback
        self.last_detection_time = time.time()
        self.timer_running = False  # Inicializar el atributo timer_running en False

    def detect_qr_code(self, frame):
        # Decodifica la imagen QR
        decoded_objects = decode(frame)
        
        # Itera sobre los objetos decodificados
        for obj in decoded_objects:
            # Verifica si los datos decodificados son de tipo texto
            if obj.type == 'QRCODE':
                # Comprueba el tiempo transcurrido desde la última detección
                current_time = time.time()
                if current_time - self.last_detection_time >= 2:
                    # Llama al callback con el nombre decodificado y el frame
                    self.callback(obj.data.decode(), frame, self)
                    self.last_detection_time = current_time

def leer_qr_camara(callback):
    # Inicializa la cámara web
    cap = cv2.VideoCapture(0)
    detector = QRDetector(callback)

    # Inicializar pygame para reproducir audio
    pygame.init()
    pygame.mixer.init()
    sound = pygame.mixer.Sound("Windows 12 Startup Sound (mp3cut.net).mp3")  # Ruta al archivo de audio

    # Bucle de eventos
    while True:
        # Lee el siguiente frame de la cámara
        ret, frame = cap.read()

        # Si no se pudo leer el frame, sal del bucle
        if not ret:
            break

        # Muestra la vista previa de la cámara en una ventana
        cv2.imshow('Camara', frame)

        # Detecta el código QR en el frame
        detector.detect_qr_code(frame)

        # Espera 1 milisegundo y verifica si se ha presionado la tecla 'q' para salir
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Libera la cámara y cierra las ventanas abiertas de OpenCV
    cap.release()
    cv2.destroyAllWindows()

# Función de callback para manejar el nombre decodificado y el frame
def handle_decoded_name(nombre, frame, detector, sound):
    print("Nombre decodificado:", nombre)
    cv2.putText(frame, 'OK', (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)  # Muestra 'OK' en la ventana
    cv2.imshow('Camara', frame)
    
    # Reproducir audio
    sound.play()

    # Espera 2 segundos antes de cerrar la ventana
    if not detector.timer_running:  # Acceder al atributo timer_running desde una instancia de QRDetector
        threading.Timer(2.0, cv2.destroyAllWindows).start()
        detector.timer_running = True

# Inicializar pygame para reproducir audio
pygame.init()
pygame.mixer.init()
sound = pygame.mixer.Sound("Windows 12 Startup Sound (mp3cut.net).mp3")  # Ruta al archivo de audio

# Lee el nombre decodificado desde la cámara web utilizando el callback
leer_qr_camara(lambda nombre, frame, detector: handle_decoded_name(nombre, frame, detector, sound))
