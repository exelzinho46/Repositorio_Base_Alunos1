

import site
import time
import pyautogui as at


at.FAILSAFE = True


at.hotkey("win", "r")
time.sleep(1) 




at.write("chrome", interval=0.1)
at.press("enter")
time.sleep(3) 
at.write("deadshot.io", interval=0.1)
   
at.write(site, interval=0.1)
at.press("enter")
time.sleep(5) 

    
    
