import pyautogui
button7location = pyautogui.locateOnScreen('button.png') # returns (left, top, width, height) of matching region
button7location (1416, 562, 50, 41)
buttonx, buttony = pyautogui.center(button7location)
buttonx, buttony (1441, 582)

pyautogui.click(buttonx, buttony)  # clicks the center of where the button was found