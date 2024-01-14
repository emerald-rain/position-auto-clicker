import pyautogui
import keyboard
import time

# Список для хранения координат и задержек
coordinates = []
delays = []

# Флаг для управления состоянием автоклика
auto_clicking = False

print("Нажмите F7 для записи координаты, Enter для продолжения.")

# Функция для записи координаты
def record_coordinate():
    x, y = pyautogui.position()
    coordinates.append((x, y))
    delay = float(input(f"Введите задержку после клика на координате {x}, {y}: "))
    delays.append(delay)
    print(f"Координата {x}, {y} с задержкой {delay} секунд добавлена.")

# Ожидание нажатия F7 для записи координаты
while True:
    if keyboard.is_pressed('f7'):
        record_coordinate()
        time.sleep(0.2)  # небольшая задержка, чтобы избежать множественных записей
    elif keyboard.is_pressed('enter'):
        break

print("Нажмите F8 для начала/остановки автоклика.")

# Основной цикл автоклика
while True:
    if keyboard.is_pressed('f8'):
        auto_clicking = not auto_clicking
        print("Автокликер", "запущен." if auto_clicking else "остановлен.")
        time.sleep(0.1)  # небольшая задержка, чтобы избежать множественных записей

    if auto_clicking:
        for (x, y), delay in zip(coordinates, delays):
            pyautogui.click(x, y)
            time.sleep(delay)

    if keyboard.is_pressed('esc'):  # Выход из скрипта по нажатию Esc
        break
