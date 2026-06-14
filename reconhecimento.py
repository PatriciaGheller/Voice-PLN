import speech_recognition as sr
import os
from comandos import abrir_navegador, abrir_excel, abrir_powerpoint, abrir_edge, fechar_programa
from apis import previsao_tempo, tocar_playlist, ultimas_noticias

def ouvir_microfone():
    microfone = sr.Recognizer()
    with sr.Microphone() as source:
        microfone.adjust_for_ambient_noise(source)
        print("Diga alguma coisa: ")
        audio = microfone.listen(source)

    try:
        frase = microfone.recognize_google(audio, language='pt-BR')
        print("Você disse: " + frase)

        # Executa comandos conforme palavras-chave
        if "navegador" in frase:
            abrir_navegador()
        elif "Excel" in frase:
            abrir_excel()
        elif "PowerPoint" in frase:
            abrir_powerpoint()
        elif "Edge" in frase:
            abrir_edge()
        elif "Fechar" in frase:
            return fechar_programa()
        elif "clima" in frase:
            return previsao_tempo()
        elif "notícias" in frase:
            return ultimas_noticias()
        elif "música" in frase or "playlist" in frase:
            return tocar_playlist()

        return frase

    except sr.UnknownValueError:
        print("Não entendi o que você disse.")
        return None
    except sr.RequestError:
        print("Erro ao se conectar com o serviço de reconhecimento.")
        return None
