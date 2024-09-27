import os
import pyautogui
import time

os.environ['DISPLAY'] = ':0'

def open_whatsapp():
    # Open WhatsApp using the Windows search
    pyautogui.hotkey('win', 's')
    time.sleep(1)
    pyautogui.write('WhatsApp')
    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(5)

def select_contact(contact_name):
    # Open the search box in WhatsApp
    time.sleep(1)
    pyautogui.write(contact_name)
    time.sleep(2)  # Allow time for search results to appear

    contact_select = (200, 200)  
    pyautogui.click(contact_select)
    
    # Select the first contact from the search results
    pyautogui.press('enter')
    time.sleep(2)

def send_message(message):
    # Type the message and press enter
    message_box_position = (400, 800)  
    pyautogui.click(message_box_position)

    pyautogui.write(message)
    pyautogui.press('enter')

contact_name = 'Edd'
message_to_send = "Hello, how are you?"

open_whatsapp()
select_contact(contact_name)
send_message(message_to_send)