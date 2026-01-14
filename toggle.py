#!/usr/bin/env python3

import sys, time
import pyautogui as g
from tkinter import messagebox

screen_size = g.size()
if not screen_size == (1920,1080):
	messagebox.showwarning(title="Replay switch", message="Unsupported screen size.")
	sys.exit(1)

try:
	g.hotkey("alt","z")
	time.sleep(1)

	# locate replays section
	x, y = (240,350)
	g.moveTo(x,y)
	g.click()

	time.sleep(1)

	# locate toggle switch
	x, y = (486,98)
	if not g.pixelMatchesColor(x,y,(118,185,0),tolerance=5):
		g.moveTo(x,y,2)
		g.click()

	g.press("esc")
	g.press("esc")

	sys.exit(0)
except Exception as e:
	messagebox.showwarning(title="Replay switch", message=e)
	sys.exit(1)
