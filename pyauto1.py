#spiral

import pyautogui
import time

time.sleep(5)
distance=400

while distance>0:
	pyautogui.dragRel(distance,0,duration=0.5)

	distance=distance-30
	pyautogui.dragRel(0,distance,duration=0.5)
	pyautogui.dragRel(-distance,0,duration=0.5)

	distance=distance-30
	pyautogui.dragRel(0,-distance,duration=0.5)