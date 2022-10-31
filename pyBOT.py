from cgitb import text
import pyautogui
import time

#Opening  browser;
pyautogui.alert("RUNING SCRIPT!")
pyautogui.PAUSE = 0.2
pyautogui.press('winleft')
pyautogui.write('vivaldi')
pyautogui.press('enter')

#Acessing Google drive;
time.sleep(1)
pyautogui.click(x=2200, y=45)
time.sleep(1)
pyautogui.write("https://drive.google.com/drive/u/0/folders/19AeS-NlDWqN01yLvZNwFDK65U2GeEiMb")
pyautogui.press('enter')

#Opening desktop;
time.sleep(1)
pyautogui.hotkey('winleft', 'd')

#Renameing the backupfile
fileName = pyautogui.prompt(text='YOU NEED TO RENAME YOUR FILE USE THE FOLLOWING STANDART: backupfile DD.MM.AA', title='Set your file name', default='backupfile DD.MM.AA')
time.sleep(1)
pyautogui.rightClick(x=950, y=534)
pyautogui.click(x=1028, y=947)
pyautogui.write(fileName)
pyautogui.press('enter')
time.sleep(1)

#Drag the file to google drive
pyautogui.hotkey('alt', 'tab')
pyautogui.rightClick(x=2694, y=410)
pyautogui.click(x=2833, y=485)
pyautogui.click(x=2001, y=232)
pyautogui.click(x=2172, y=186)
pyautogui.press('enter')

pyautogui.alert("DONE!")


