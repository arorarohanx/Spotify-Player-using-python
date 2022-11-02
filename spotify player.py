import pyautogui as pg
import time
song = input("Enter the name of your song (if possible add singer name after song name for precise result) :-")
pg.hotkey("win")
pg.typewrite("spotify")
time.sleep(1)
pg.typewrite(["enter"])
time.sleep(2)

if "spotify":
    time.sleep(2)
    pg.moveTo(415,259,duration=0.5)
    pg.click()
    time.sleep(1)
    pg.typewrite(song)
    time.sleep(1.5)
    pg.moveTo(1159,385,duration=0)
    pg.click()
    time.sleep(0.5)
    pg.moveTo(1322,850)
    pg.click()
else:
    exit()
    