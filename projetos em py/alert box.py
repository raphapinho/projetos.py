from curses import BUTTON_ALT
import pyautogui 


#pyautogui.alert("isso é um caixa de alerta")

''' press = pyautogui.confirm("enter option", buttons=["a","b","c"])

    if press  == 'a':
        pyautogui.alert("cê é louco meu irmão")
    elif press == 'b':
        pyautogui.alert('tenta de novo coroa')
    else:
        pyautogui.alert("seriozão isso?")'''

'''tab=pyautogui.prompt("qual o seu nome?")
pyautogui.alert(f"Olá, {tab}")'''

senha = pyautogui.password('entre com a senha:')

if senha == "1234":
    pyautogui.alert("seja bem vindo")
else
    pyautogui.alert("tente de novo")