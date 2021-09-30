import pyscreenshot as ImageGrab
import time


def screenshot(s):
   time.sleep(3)
   ss = ImageGrab.grab(bbox=(0, 0, 1920, 1080))
   ss.save(s + ".png")