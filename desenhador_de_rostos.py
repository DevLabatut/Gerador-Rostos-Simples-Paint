import pyautogui
import time

def desenhar_cinco_rostos():
    time.sleep(2)

    x_inicial, y_inicial = pyautogui.position()

    tamanho_rosto = 100
    tamanho_olho = 15
    tamanho_nariz = 20
    tamanho_boca = 30
    espacamento_olhos = 20
    espacamento_entre_rostos = 50

    for i in range(5):
        x_atual = x_inicial + i * (tamanho_rosto + espacamento_entre_rostos)
        desenhar_rosto(x_atual, y_inicial, tamanho_rosto, tamanho_olho, tamanho_nariz, tamanho_boca, espacamento_olhos)

def desenhar_rosto(x, y, tamanho_rosto, tamanho_olho, tamanho_nariz, tamanho_boca, espacamento_olhos):

    pyautogui.moveTo(x - tamanho_rosto // 2, y - tamanho_rosto // 2, duration=0.1)
    pyautogui.dragRel(tamanho_rosto, 0, duration=0.1)
    pyautogui.dragRel(0, tamanho_rosto, duration=0.1)
    pyautogui.dragRel(-tamanho_rosto, 0, duration=0.1)
    pyautogui.dragRel(0, -tamanho_rosto, duration=0.1)

    x_olho_esquerdo = x - espacamento_olhos - tamanho_olho // 2
    y_olho = y - tamanho_rosto // 4
    pyautogui.moveTo(x_olho_esquerdo, y_olho, duration=0.1)
    pyautogui.dragRel(tamanho_olho, 0, duration=0.1)

    x_olho_direito = x + espacamento_olhos - tamanho_olho // 2
    pyautogui.moveTo(x_olho_direito, y_olho, duration=0.1)
    pyautogui.dragRel(tamanho_olho, 0, duration=0.1)

    x_nariz = x - tamanho_nariz // 2
    y_nariz = y
    pyautogui.moveTo(x_nariz, y_nariz, duration=0.1)
    pyautogui.dragRel(tamanho_nariz, 0, duration=0.1)

    x_boca = x - tamanho_boca // 2
    y_boca = y + tamanho_rosto // 4
    pyautogui.moveTo(x_boca, y_boca, duration=0.1)
    pyautogui.dragRel(tamanho_boca, 0, duration=0.1)

if __name__ == "__main__":
    desenhar_cinco_rostos()
