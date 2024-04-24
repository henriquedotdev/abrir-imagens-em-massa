import os
import webbrowser
from tkinter import Tk, filedialog

def abrir_arquivos_png_em_chrome():
    root = Tk()
    root.withdraw() 

    pasta = filedialog.askdirectory(title="Selecione a pasta com os arquivos PNG")

    if not pasta:
        print("Nenhuma pasta selecionada. Encerrando o programa.")
        return

    arquivos = os.listdir(pasta)

    for arquivo in arquivos:
        if arquivo.lower().endswith(".png"):
            caminho_completo = os.path.join(pasta, arquivo)
            webbrowser.open("file:///" + caminho_completo, new=2)

abrir_arquivos_png_em_chrome()
