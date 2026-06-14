import pyttsx3
from src.feedback import falar

# Inicializa o motor de voz
engine = pyttsx3.init()


def mensagem_boas_vindas():
    falar("Bem-vindo ao Voice-PLN! Seu assistente de voz está pronto para ajudar.")


def falar(texto):
    """Faz o computador falar o texto informado"""
    engine.say(texto)
    engine.runAndWait()

def confirmar_acao(acao):
    """Confirma a ação executada com voz"""
    falar(f"Abrindo {acao}...")

def encerrar():
    """Mensagem sonora de encerramento"""
    falar("Encerrando o sistema Voice-PLN. Até logo!")
