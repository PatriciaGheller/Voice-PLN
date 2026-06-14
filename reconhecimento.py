import speech_recognition as sr
import os

# Função para ouvir e reconhecer a fala
def ouvir_microfone():
    microfone = sr.Recognizer()

    with sr.Microphone() as source:
        # Reduz ruídos do ambiente
        microfone.adjust_for_ambient_noise(source)
        print("Diga alguma coisa: ")

        # Captura o áudio
        audio = microfone.listen(source)

    try:
        # Reconhece a fala usando o Google
        frase = microfone.recognize_google(audio, language='pt-BR')
        print("Você disse: " + frase)

        # Executa comandos conforme palavras-chave
        if "navegador" in frase:
            os.system("start chrome.exe")
        elif "Excel" in frase:
            os.system("start excel.exe")
        elif "PowerPoint" in frase:
            os.system("start powerpnt.exe")
        elif "Edge" in frase:
            os.system("start msedge.exe")
        elif "Fechar" in frase:
            print("Encerrando programa...")
            return True

    except sr.UnknownValueError:
        print("Não entendi o que você disse.")
    except sr.RequestError:
        print("Erro ao se conectar com o serviço de reconhecimento.")

    return False
