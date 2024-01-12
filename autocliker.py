import pyautogui
import time

# Функция для получения координат двух кликов
def get_click_coordinates():
    time.sleep(0.5)  # Пауза между кликами
    print("Пожалуйста, кликните по двум точкам.")
    
    # Получаем первую координату
    first_click = pyautogui.position()
    print("Координаты первого клика:", first_click)
    
    # Ожидаем второй клик
    input("Нажмите Enter после выполнения второго клика...")
    
    # Получаем вторую координату
    second_click = pyautogui.position()
    print("Координаты второго клика:", second_click)
    
    return first_click, second_click

# Функция для повторения кликов каждые 5 секунд
def repeat_clicks(coordinates):
    while True:
        for coord in coordinates:
            pyautogui.click(coord[0], coord[1])
            time.sleep(0.5)  # Пауза между кликами
        time.sleep(2)  # Пауза между повторениями

if __name__ == "__main__":
    # Получаем координаты двух кликов
    click_coordinates = get_click_coordinates()
    
    # Запускаем бесконечный цикл повторения кликов
    repeat_clicks(click_coordinates)
