#an amazing amazing program/ feature to kill someone's buzz.
import pyautogui, time
time.sleep(5)
f = open("lyric.txt", 'r')
for word in f:
    pyautogui.typewrite(word)
    pyautogui.press("enter")




