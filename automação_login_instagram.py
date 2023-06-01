import time
import pyautogui
from selenium.webdriver import Chrome


#abertura do navegador
url="https://www.instagram.com/"
navegador = Chrome()
navegador.get(url)


#Tela cheia
pyautogui.hotkey("fn","f11")

#Colocando o login
pyautogui.moveTo(1200,330,1)
pyautogui.leftClick()
time.sleep(1)
pyautogui.hotkey("o","t","a","v","i","o")
time.sleep(1)

#colocando a senha e entrnado
pyautogui.moveTo(1200,380,1)
pyautogui.leftClick()
time.sleep(1)
pyautogui.hotkey("e","x","e","m","p","l","o")
pyautogui.moveTo(1320,380,1)
pyautogui.leftClick()
pyautogui.moveTo(1300,430,1)
pyautogui.leftClick()
time.sleep(6)













