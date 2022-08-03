import pyautogui
import time
import random

i=0
while True:
	print("Python is controlling cursor from "+ repr(i) +"secs...")
	pyautogui.moveTo(random.randint(200,800),random.randint(200,800))
	pyautogui.click()
	time.sleep(30)
	i=i+30;
