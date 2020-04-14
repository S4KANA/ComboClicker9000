import pyautogui
import pyWinhook
import pythoncom
import time

def OnKeyboardEvent(event):
    if int(event.Ascii) == 120: #wx
        global exit
        print("[-] Exit button pressed")
        exit = True

    if int(event.Ascii) == 32: # space bar
        global first_pos
        global second_pos

        if first_pos[0] == -1:
            first_pos = pyautogui.position()
            print("[+] First position set")
        elif second_pos[0] == -1:
            second_pos = pyautogui.position()
            print("[+] Second position set")
    return True

def guide():
    print("")
    print("1) Put your cursor on the combo creature and press the 'Space bar' key")
    print("2) Click the creature and move your cursor to the wability box, then press the 'space bar' key again")
    print("3) Press 'x' to stop the clicking (may have to press it multiple times)")


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
            if exit:
                first_pos = (-1, -1)
                second_pos = (-1, -1)
                guide()
                exit = False
                break
            pythoncom.PumpWaitingMessages()
            pyautogui.press('w') # auto mana hotkey
            pyautogui.click(first_pos[0], first_pos[1])
            time.sleep(0.1)
            pyautogui.click(second_pos[0], second_pos[1])

if __name__ == "__main__":
    main()
