import os
import pyautogui
import time

os.environ['DISPLAY'] = ':0'

def open_whatsapp():
   
    pyautogui.hotkey('win', 's')
    time.sleep(1)
    pyautogui.write('WhatsApp')
    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(2)

def select_contact(contact_name):
    
    pyautogui.hotkey('ctrl', 'f') 
    time.sleep(1)
    pyautogui.write(contact_name) 
    time.sleep(2) 

    pyautogui.press('down') 
    time.sleep(1) 
    pyautogui.press('enter')  
    time.sleep(2)  

def send_message(message):
    
    pyautogui.write(message)
    pyautogui.press('enter')

contact_name = 'Tunn Sawari'
message = "This is an automated message"

open_whatsapp() 
select_contact(contact_name) 
send_message(message)