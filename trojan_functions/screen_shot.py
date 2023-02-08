import pyautogui

def screen_shot():
    myScreenshot = pyautogui.screenshot()
    myScreenshot.save(r'photo.png')
