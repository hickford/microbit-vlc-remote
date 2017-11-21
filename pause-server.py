import win32api # pip install pypiwin32
from win32gui import GetWindowText, GetForegroundWindow

KEYEVENTF_KEYUP = 0x0002 # https://msdn.microsoft.com/en-us/library/windows/desktop/ms646304(v=vs.85).aspx
VK_MEDIA_PLAY_PAUSE = 0xB3 # https://msdn.microsoft.com/en-us/library/windows/desktop/dd375731(v=vs.85).aspx
VK_SPACE = 0x20
VK_SHIFT = 0x10

VK_MENU = 0x12 # alt
VK_LEFT = 0x25

def in_netflix():
    window_text = GetWindowText(GetForegroundWindow())
    return "Netflix" in window_text

def play_pause():
    """Toggle play. Assumes media player is focused."""
    key = VK_SPACE if in_netflix() else VK_MEDIA_PLAY_PAUSE
    win32api.keybd_event(key, 0)

def rewind_ten_seconds():
    key_to_hold = VK_SHIFT if in_netflix() else VK_MENU
    win32api.keybd_event(key_to_hold, 0)
    win32api.keybd_event(VK_LEFT, 0)
    win32api.keybd_event(key_to_hold, 0, KEYEVENTF_KEYUP)

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
