import webbrowser
import time
import pyautogui
import urllib.request
import json

while True:
    obj = json.loads(urllib.request.urlopen('http://api.open-notify.org/iss-now.json').read())

    lat = obj['iss_position']['latitude']
    long = obj['iss_position']['longitude']

    webbrowser.open("ISS_Live_Video.html")

    time.sleep(20)

    pyautogui.screenshot(lat + '_' + long + '.png', region = (135,105,1644,924))

    pyautogui.hotkey('ctrl', 'w')

    time.sleep(5*60)

