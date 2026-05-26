import pyautogui as at

at.hotkey("win", "r")
at.write("mspaint")
at.press("enter")
at.sleep(3)
at.mouseDown(0,0)
at.moveTo(500,500)