import pyttsx3

# Inicializa o motor de voz
engine = pyttsx3.init()

# Lista todas as vozes disponíveis
voices = engine.getProperty('voices')

# Seleciona automaticamente uma voz em português Brasil, se existir
voz_selecionada = None
for voice in voices:
    if "Portuguese" in voice.name or "Brazil" in voice.name:
        voz_selecionada = voice
        break

# Se encontrou voz em português, usa ela; senão, mantém a padrão
if voz_selecionada:
    engine.setProperty('voice', voz_selecionada.id)

# Configura velocidade e volume
engine.setProperty('rate', 180)   # velocidade da fala (padrão ~200)
engine.setProperty('volume', 1.0) # volume máximo (0.0 a 1.0)

def mensagem_boas_vindas():
    """Mensagem inicial de boas-vindas"""
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

def listar_vozes():
    """Lista todas as vozes disponíveis no sistema"""
    for i, voice in enumerate(voices):
        print(f"{i}: {voice.name} - {voice.id}")
