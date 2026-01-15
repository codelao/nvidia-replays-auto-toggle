#!/usr/bin/env python3

"""
> Nvidia replays auto toggle
> By CodeLao
> Licensed under MIT

https://github.com/codelao/nvidia-replays-auto-toggle
"""

import os, sys, cv2, time, csv
import pyautogui as g
from tkinter import messagebox

def count_in(path: str) -> bool:
	config = os.path.join(path, "config.csv")
	if not os.path.isfile(config):
		return False
	with open(config, "r") as c:
	    rows = list(csv.reader(c))
	    if len(rows)!=2 or len(rows[1])!=1:
	    	return False
	    seconds = rows[1][0]
	try:
		seconds = int(seconds)
	except ValueError:
		try:
			seconds = float(seconds)
		except ValueError:
			return False
	if seconds>=0 and seconds<=15:
		time.sleep(seconds)
		return True
	else:
		return False

try:
	screen_size = g.size()
	if not screen_size == (1920,1080):
		raise SystemError("Unsupported resolution. You can only use this tool on 1920x1080 screen.")

	__path__ = os.path.dirname(sys.executable)
	if not count_in(__path__):
		raise ValueError("Cannot configure count-in. Fix or reset your config.csv file (see installation folder).")

	# open overlay
	g.hotkey("alt","z")
	time.sleep(1)

	# make sure overlay is opened
	try:
		g.locateOnScreen("overlay-marker.png", confidence=0.8)
	except g.ImageNotFoundException:
		raise SystemError("NVIDIA App is either not installed or not running yet. Also, make sure that your overlay's hotkey is set to Alt+Z, otherwise, you will not be able to use this tool.")
	
	# locate replays section
	x, y = (240,350)
	g.moveTo(x,y)
	g.click()

	time.sleep(1)

	# locate toggle switch
	x, y = (486,98)
	if not g.pixelMatchesColor(x,y,(118,185,0),tolerance=20):
		g.moveTo(x,y,2)
		g.click()

	# close overlay
	g.press("esc")
	g.press("esc")

	sys.exit(0)
except Exception as e:
	messagebox.showwarning(title="Replay switch", message=e)
	sys.exit(1)
