import os
import time
import json

appDarkCmd = 'start /b reg.exe add HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\Themes\Personalize /v AppsUseLightTheme /t REG_DWORD /d 0 /f'
appLightCmd = 'start /b reg.exe add HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\Themes\Personalize /v AppsUseLightTheme /t REG_DWORD /d 1 /f'
sysDarkCmd = 'start /b reg.exe add HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\Themes\Personalize /v SystemUsesLightTheme /t REG_DWORD /d 0 /f'
sysLightCmd = 'start /b reg.exe add HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\Themes\Personalize /v SystemUsesLightTheme /t REG_DWORD /d 1 /f'

current_status = "Dark"

while True:
    with open("setting.json", "r") as f:
        data = json.load(f)
    current_time = int(time.strftime("%H%M"))
    light_time = int(time.strftime("%H%M", time.strptime(data["light-time"], "%H:%M")))
    dark_time = int(time.strftime("%H%M", time.strptime(data["dark-time"], "%H:%M")))
    # Light
    if light_time < current_time < dark_time:
        if current_status == "Light":
            pass
        else:
            current_status = "Light"
            if data["sys-light"] is True: os.system(sysLightCmd)
            if data["app-light"] is True: os.system(appLightCmd)
        print("Light Mode")
    # Dark
    else:
        if current_status == "Dark":
            pass
        else:
            current_status = "Dark"
            if data["sys-dark"] is True: os.system(sysDarkCmd)
            if data["app-dark"] is True: os.system(appDarkCmd)
        print("Dark Mode")
    time.sleep(60)
