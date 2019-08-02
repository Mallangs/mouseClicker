#    made by mallang   #
# Simple Mouse Clicker #
#      2019 08 02      #

import pyautogui as pag
from pynput.mouse import Controller

def moveMouse(x ,y):
	pag.moveTo(x, y, 1)
	#clicker()

def keepPosition():
	global x1, y1
	x1 = Controller().position[0]
	y1 = Controller().position[1]


def clickCount():
	count = input("how many click?")

	for i in range(0, int(count)):
		if x1 != Controller().position[0] or y1!= Controller().position[1]:
			moveMouse(x1, y1)
		pag.click()
	
keepPosition()
clickCount()
# if you want More Click then use While or for 
