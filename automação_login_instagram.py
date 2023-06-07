
import time
import pyautogui
import tkinter as tk
from tkinter import messagebox
from tkinter import simpledialog
from selenium.webdriver import Chrome



#verifica se o usuario tem o login armazenado
try:
    with open("login.txt", "r") as file:
      login_armazenado=file.readline().strip()
except FileNotFoundError:
   login_armazenado=""

#caso não tenha ele não tenha os armazena
if not login_armazenado:
   root =tk.Tk()
   root.withdraw()
   login= simpledialog.askstring("Gmail","Digite o seu Gmail")

   with open("login.txt","w") as file:
      file.write(login)
else:
   print(login_armazenado)

#=============================================================================================

#verifica se o usuario tem senha armazenada
try:
    with open("senha.txt", "r") as file:
      senha_armazenado=file.readline().strip()
except FileNotFoundError:
   senha_armazenado=""

#caso não tenha ele não tenha os armazena
if not senha_armazenado:
   root =tk.Tk()
   root.withdraw()
   senha= simpledialog.askstring("Senha","Digite a sua Senha")

   with open("senha.txt","w") as file:
      file.write(senha)
else:
   print(senha_armazenado)


#abertura do navegador
url="https://www.instagram.com/"
navegador = Chrome()
navegador.get(url)


#Tela cheia
pyautogui.hotkey("fn","f11")
time.sleep(1)

#Colocando o login
pyautogui.moveTo(1200,320,1)
pyautogui.leftClick()
time.sleep(1)
pyautogui.typewrite(login_armazenado)
time.sleep(1)

#colocando a senha e entrnado
pyautogui.moveTo(1200,380,1)
pyautogui.leftClick()
time.sleep(1)
pyautogui.typewrite(senha_armazenado)
pyautogui.moveTo(1320,380,1)
pyautogui.leftClick()
pyautogui.moveTo(1300,430,1)
pyautogui.leftClick()
time.sleep(1)
pyautogui.moveTo(100,200,1)
time.sleep(5)
pyautogui.leftClick()
pyautogui.moveTo(950,690,1)
time.sleep(2)
pyautogui.leftClick()


#timer que a sua pagina ficara aberta!!
time.sleep(20)














