import os
from src.feedback import confirmar_acao, encerrar

def abrir_navegador():
    print("Abrindo navegador Chrome...")
    confirmar_acao("navegador Chrome")
    os.system("start chrome.exe")

def abrir_excel():
    print("Abrindo Excel...")
    confirmar_acao("Excel")
    os.system("start excel.exe")

def abrir_powerpoint():
    print("Abrindo PowerPoint...")
    confirmar_acao("PowerPoint")
    os.system("start powerpnt.exe")

def abrir_edge():
    print("Abrindo Microsoft Edge...")
    confirmar_acao("Microsoft Edge")
    os.system("start msedge.exe")

def fechar_programa():
    print("Encerrando Voice-PLN...")
    encerrar()
    return True
