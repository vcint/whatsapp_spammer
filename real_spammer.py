import pyautogui
import webbrowser as wb
import time
wb.open('web.whatsapp.com')
time.sleep(20)
while True:
  pyautogui.hotkey('ctrl','v')
  pyautogui.press("enter")
  time.sleep(5)