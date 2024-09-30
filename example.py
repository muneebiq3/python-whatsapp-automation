import os
import pyautogui
import time
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)

os.environ['DISPLAY'] = ':0'

def open_whatsapp():
    try:
        logging.info("Opening WhatsApp...")
        pyautogui.hotkey('win', 's')  # Windows search bar
        time.sleep(1)
        pyautogui.write('WhatsApp')  # Type WhatsApp
        time.sleep(1)
        pyautogui.press('enter')  # Press Enter to open WhatsApp
        time.sleep(5)  # Wait for WhatsApp to open fully
    except Exception as e:
        logging.error(f"Error opening WhatsApp: {e}")

def select_contact(contact_name):
    try:
        logging.info(f"Searching for contact: {contact_name}")
        pyautogui.hotkey('ctrl', 'f')  # Open search bar in WhatsApp
        time.sleep(1)
        pyautogui.write(contact_name)  # Type contact name
        time.sleep(2)  # Wait for search results to appear

        # Example: Replace these coordinates with the actual ones
        contact_coordinates = (153, 184)  # Update this with your own coordinates
        logging.info(f"Clicking on contact at {contact_coordinates}")
        pyautogui.click(contact_coordinates)  # Click on the first search result
        time.sleep(2)  # Wait for the chat to open fully
        logging.info(f"Contact {contact_name} selected.")
    except Exception as e:
        logging.error(f"Error selecting contact: {e}")

def send_message(message):
    try:
        logging.info("Typing and sending message...")
        pyautogui.write(message)  # Type the message
        pyautogui.press('enter')  # Press Enter to send the message
        logging.info("Message sent.")
    except Exception as e:
        logging.error(f"Error sending message: {e}")

# Main script
contact_name = input("Enter the contact name: ")  # Get the contact name from the user
message = input("Enter the message: ")  # Get the message from the user

open_whatsapp()  
select_contact(contact_name)  
send_message(message)
