import pyautogui, time
time.sleep(5)
f = open("marijuana.txt", 'r')
for i in f:
    i = i.rstrip()
    if len(i) > 0:
        i = i.split()
        for j in i:
            pyautogui.write(str(j))
            pyautogui.press("enter")



    
    