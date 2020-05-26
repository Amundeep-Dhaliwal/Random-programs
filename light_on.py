#!python3

import pyautogui, time
pyautogui.PAUSE = 0.5

pyautogui.press('win')
pyautogui.typewrite('hue sync')
pyautogui.press('enter')


#time.sleep(9)
while True:
    try:
        switchx, switchy = pyautogui.locateCenterOnScreen(r"C:\Users\Amundeep\Pictures\Camera Roll\light_switch.PNG")
    except TypeError:
        continue
    else:
        break

pyautogui.click(switchx, switchy)
time.sleep(0.5)
pyautogui.hotkey('alt', 'f4')


