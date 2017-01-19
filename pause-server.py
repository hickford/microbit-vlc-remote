import win32api # pip install pypiwin32

KEYEVENTF_KEYUP = 0x0002 # https://msdn.microsoft.com/en-us/library/windows/desktop/ms646304(v=vs.85).aspx
VK_MEDIA_PLAY_PAUSE = 0xB3 # https://msdn.microsoft.com/en-us/library/windows/desktop/dd375731(v=vs.85).aspx

VK_MENU = 0x12 # alt
VK_LEFT = 0x25

def play_pause():
    """Toggle play. Assumes media player is focused."""
    win32api.keybd_event(VK_MEDIA_PLAY_PAUSE, 0)

def rewind_ten_seconds():
    win32api.keybd_event(VK_MENU, 0)
    win32api.keybd_event(VK_LEFT, 0)
    win32api.keybd_event(VK_MENU, 0, KEYEVENTF_KEYUP)

import serial # pip install pyserial
from serial.tools.list_ports import comports

def find_microbit_comport():
    for p in comports():
        if p.pid == 516 and p.vid == 3368:
            return p.device

port = find_microbit_comport()
if not port:
    raise OSError("No microbit plugged in")

with serial.Serial(port, baudrate=115200) as s:
    print(s)

    while True:
        message = s.readline().decode('utf8').strip()
        print(message)
        if "A" in message:
            play_pause()
        elif "B" in message:
            rewind_ten_seconds()
