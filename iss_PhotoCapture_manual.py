import webbrowser
from time import sleep
import pyautogui
import iss_location

def main():
    webbrowser.open("https://iss-live.github.io")

    sleep(20) # Page Load Time

    pyautogui.screenshot(str(iss_location.lat() + '_' + iss_location.long() + '.png'), region = (135,105,1644,924))
    pyautogui.hotkey('ctrl', 'w')


if __name__ == "main":
    main()
