import speech_recognition as sr
from src.apis import previsao_tempo_por_fala, ultimas_noticias, tocar_playlist
from src.feedback import falar
import webbrowser
import os

def ouvir_microfone():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Diga alguma coisa: ")
        audio = r.listen(source)

    try:
        frase = r.recognize_google(audio, language="pt-BR")
        print("Você disse:", frase)

        # Normaliza a frase para facilitar reconhecimento
        frase_lower = frase.lower()

        # ==========================
        # Comandos de Navegador
        # ==========================
        if any(palavra in frase_lower for palavra in ["navegador", "abrir navegador", "chrome", "google"]):
            falar("Abrindo navegador Chrome...")
            webbrowser.open("https://www.google.com")
            return "Navegador aberto"

        # ==========================
        # Comandos de Excel
        # ==========================
        elif any(palavra in frase_lower for palavra in ["excel", "planilha", "abrir excel"]):
            falar("Abrindo Excel...")
            os.system("start excel")
            return "Excel aberto"

        # ==========================
        # Comandos de Música / Spotify
        # ==========================
        elif any(palavra in frase_lower for palavra in ["música", "playlist", "spotify", "tocar música"]):
            resultado = tocar_playlist()
            falar(resultado)
            return resultado

        # ==========================
        # Comandos de Clima / Previsão
        # ==========================
        elif any(palavra in frase_lower for palavra in ["previsão do tempo", "clima", "tempo", "como está o tempo"]):
            resultado = previsao_tempo_por_fala(frase)
            falar(resultado)
            return resultado

        # ==========================
        # Comandos de Notícias
        # ==========================
        elif any(palavra in frase_lower for palavra in ["notícia", "últimas notícias", "notícias de hoje", "jornal"]):
            noticias = ultimas_noticias()
            for noticia in noticias:
                falar(noticia)
            return "\n".join(noticias)

        # ==========================
        # Comando não reconhecido
        # ==========================
        else:
            falar("Não entendi o que você disse.")
            return "Comando não reconhecido"

    except sr.UnknownValueError:
        falar("Não consegui entender o que você disse.")
        return "Erro: fala não reconhecida"

    except sr.RequestError as e:
        falar("Erro ao se conectar ao serviço de reconhecimento de voz.")
        return f"Erro: {e}"