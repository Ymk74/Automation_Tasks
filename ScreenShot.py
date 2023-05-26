
import pyautogui
import time

counter = 1
while True:
    im = pyautogui.screenshot()
    im.save(f"Name{counter}.jpg")

    time.sleep(60) # delay 60 sec = 1 minute
    counter += 1 
    
