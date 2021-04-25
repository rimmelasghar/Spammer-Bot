#Spammer bot made by Rimmel asghar
import pyautogui,time
text=input('Enter the message Do you want to send : ')
rng=int(input('Enter the number of time do you want to spam : '))
time.sleep(10)
for i in range(rng):
    pyautogui.typewrite(text)
    pyautogui.press("enter")