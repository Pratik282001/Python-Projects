import time
from plyer import notification

if __name__ == "__main__":
    while(True):
        notification.notify(
            title="Please drink water.",
            message="About 15.5 cups (3.7 liters) of fluids for men a day",
            app_icon="D:\python projects\Iconsmind-Outline-Glass-Water.ico",
            timeout=10
        )
        time.sleep(6)

#for background running ;)
#pythonw.exe .\notification maker.py