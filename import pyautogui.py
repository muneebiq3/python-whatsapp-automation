import pyautogui
import time
# This will print your current mouse position every second
while True:
    print(pyautogui.position())
    time.sleep(1)  # Adjust the delay as needed
