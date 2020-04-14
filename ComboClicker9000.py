import pyautogui
import pyWinhook
import pythoncom
import time
from random import randrange

def OnKeyboardEvent(event):
    global first_pos
    global second_pos

    if (event.Key) == "Numpad0":
        print("[-] Exit button pressed")
        first_pos = (-1, -1)
        second_pos = (-1, -1)
        guide()
        pyautogui.keyUp('w')

    if (event.Key) == "Numpad1": # space bar
        if first_pos[0] == -1:
            first_pos = pyautogui.position()
            print("[+] First position set")
        elif second_pos[0] == -1:
            second_pos = pyautogui.position()
            print("[+] Second position set")
    return True

def guide():
    print("")
    print("1) Put your cursor on the combo creature and press the 'Numpad 1' key")
    print("2) Click the creature and move your cursor to the wability box, then press the 'space bar' key again")
    print("3) Press 'Numpad 0' to stop the clicking (may have to press it multiple times)")


# globals
first_pos = (-1, -1)
second_pos = (-1, -1)
exit = False

def main():
    hm = pyWinhook.HookManager()
    hm.KeyDown = OnKeyboardEvent
    hm.HookKeyboard()
    guide()

    while True:
        pythoncom.PumpWaitingMessages()
        global first_pos
        global second_pos
        global exit
        while first_pos[0] != -1 and second_pos[0] != -1:
            pythoncom.PumpWaitingMessages()
            pyautogui.keyDown('w')
            next_pos = (first_pos[0], first_pos[1])
            if(next_pos[0] != -1):
                pyautogui.click(next_pos[0], next_pos[1])
            time.sleep(0.1)
            next_pos = (second_pos[0], second_pos[1])
            if (next_pos[0] != -1):
                pyautogui.click(next_pos[0], next_pos[1])

if __name__ == "__main__":
    main()
