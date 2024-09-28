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
    time.sleep(5)  # Give time for WhatsApp to open

def select_contact(contact_name):
    # Open the search box in WhatsApp
    pyautogui.hotkey('ctrl', 'f')  # Open search bar
    time.sleep(1)
    pyautogui.write(contact_name)  # Type the contact name
    time.sleep(2)  # Wait for search results to appear
    
    # Click on the first contact in the search result
    # You may need to adjust these coordinates based on your screen resolution and WhatsApp layout.
    contact_position = (935, 232)  # Coordinates for the first contact in search results
    pyautogui.click(contact_position)  # Click on the contact
    time.sleep(2)  # Wait for the chat to open

def send_message(message):
    # Type the message and press Enter to send
    pyautogui.write(message)
    pyautogui.press('enter')

# Main script
contact_name = input("Enter the contact name: ")  # Get contact name from the user
message = input("Enter the message: ")  # Get message from the user

open_whatsapp()  
select_contact(contact_name)  
send_message(message)
