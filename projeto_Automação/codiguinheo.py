
import pyautogui
import time
import pandas
# pip install pandas openpyxl
pyautogui.PAUSE = 1

# pyautogui.click 
# pyautogui.press
# pyautogui.write

pyautogui.press("win")

pyautogui.write("chrome")

pyautogui.press("enter")

time.sleep(1.5)

pyautogui.click(x=581, y=849)

pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")

pyautogui.press("enter")

time.sleep(3)

pyautogui.click(x=369, y=360)

pyautogui.write("emailzin@gmail")

pyautogui.press("tab")

pyautogui.write("senha")

pyautogui.press("tab")

pyautogui.press("enter")



tabela = pandas.read_csv("produtos.csv")



for linha in tabela.index:


    pyautogui.click(x=307, y=244)

    codigo = str(tabela.loc[linha, "codigo"])
    pyautogui.write(codigo)
    pyautogui.press("tab")

    marca = str(tabela.loc[linha, "marca"])
    pyautogui.write(marca)
    pyautogui.press("tab")
 
    tipo = str(tabela.loc[linha, "tipo"])
    pyautogui.write(tipo)
    pyautogui.press("tab")

    categoria = str(tabela.loc[linha, "categoria"])
    pyautogui.write(categoria)
    pyautogui.press("tab")

    preco_unitario = str(tabela.loc[linha, "preco_unitario"])
    pyautogui.write(preco_unitario)
    pyautogui.press("tab")

    custo = str(tabela.loc[linha, "custo"])
    pyautogui.write(custo)
    pyautogui.press("tab")


    obs = str(tabela.loc[linha, "obs"])

    if obs != "nan":
        pyautogui.write(obs)
    pyautogui.press("tab")

    pyautogui.press("enter")

    pyautogui.scroll(1000000)


