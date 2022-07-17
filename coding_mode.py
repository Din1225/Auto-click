import pyautogui
pyautogui.PAUSE = 0.8                 
#寫code的程式
pyautogui.press("winleft")
pyautogui.typewrite("visual studio code")
pyautogui.press("enter")

pyautogui.press("winleft")
pyautogui.typewrite("github desktop")
pyautogui.press("enter")

pyautogui.press("winleft")
pyautogui.typewrite("google chrome")
pyautogui.press("enter")

pyautogui.PAUSE = 1.5
pyautogui.moveTo(561,6)
pyautogui.click(561,6)
pyautogui.PAUSE = 0.8
pyautogui.typewrite("https://github.com/Din1225?tab=repositories")
pyautogui.press("enter")

# pyautogui.press("winleft")
# pyautogui.typewrite("discord")
# pyautogui.press("enter")

