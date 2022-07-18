import pyautogui

pyautogui.PAUSE = 0.8                
# 開寫code的程式
pyautogui.press("winleft")
pyautogui.typewrite("visual studio code")
pyautogui.press("enter")

pyautogui.press("winleft")
pyautogui.typewrite("github desktop")
pyautogui.press("enter")

pyautogui.PAUSE = 5  
pyautogui.press("winleft")
pyautogui.typewrite("cmd")
pyautogui.press("enter")
pyautogui.typewrite("jupyter notebook")
pyautogui.press("enter")

# 開github
pyautogui.PAUSE = 5
pyautogui.press("winleft")
pyautogui.PAUSE = 0.8
pyautogui.typewrite("google chrome")
pyautogui.press("enter")

pyautogui.PAUSE = 1.5
pyautogui.moveTo(201,52)
pyautogui.click(201,52)
pyautogui.typewrite("https://github.com/Din1225?tab=repositories")
pyautogui.PAUSE = 0.8
pyautogui.press("enter")

# 開Discord
pyautogui.press("winleft")
pyautogui.typewrite("discord")
pyautogui.press("enter")

