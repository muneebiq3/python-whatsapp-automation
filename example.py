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

    # Use keyboard navigation to select the first contact in the search results
    pyautogui.press('down')  # Navigate to the first search result
    time.sleep(1)  # Short delay to ensure navigation
    pyautogui.press('enter')  # Select the contact
    time.sleep(2)  # Wait for the chat to open

def send_message(message):
    # Type the message and press Enter to send
    pyautogui.write(message)
    pyautogui.press('enter')

contact_name = 'Edd'
message = "Hello, how are you?"

open_whatsapp()  # Open WhatsApp
select_contact(contact_name)  # Search and click contact chat
send_message(message)  # Send the message
