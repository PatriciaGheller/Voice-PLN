import speech_recognition as sr
from src.apis import previsao_tempo_por_fala, ultimas_noticias, tocar_playlist
from src.feedback import falar
import webbrowser
import os

def ouvir_microfone():
    r = sr.Recognizer()

    try:
        # Lista os microfones disponíveis
        dispositivos = sr.Microphone.list_microphone_names()
        print("Dispositivos de áudio disponíveis:", dispositivos)

        # Procura microfone Realtek (ajuste conforme sua máquina)
        mic_index = None
        for i, nome in enumerate(dispositivos):
            if "Microfone" in nome and "Realtek" in nome:
                mic_index = i
                break

        if mic_index is None:
            falar("Nenhum microfone válido encontrado.")
            return "Erro: microfone não encontrado"

        # Usa o microfone correto
        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source, duration=1)
            print("Diga alguma coisa: ")
            audio = r.listen(source)

        # Reconhecimento de fala
        frase = r.recognize_google(audio, language="pt-BR")
        print("Você disse:", frase)
        frase_lower = frase.lower()

        # ==========================
        # Comandos
        # ==========================
        if any(p in frase_lower for p in ["navegador", "abrir navegador", "chrome", "google"]):
            falar("Abrindo navegador Chrome...")
            webbrowser.open("https://www.google.com")
            return "Navegador aberto"

        elif any(p in frase_lower for p in ["excel", "planilha", "abrir excel"]):
            falar("Abrindo Excel...")
            os.system("start excel")
            return "Excel aberto"

        elif any(p in frase_lower for p in ["música", "playlist", "spotify", "tocar música"]):
            resultado = tocar_playlist()
            falar(resultado)
            return resultado

        elif any(p in frase_lower for p in ["previsão do tempo", "clima", "tempo", "como está o tempo"]):
            resultado = previsao_tempo_por_fala(frase)
            falar(resultado)
            return resultado

        elif any(p in frase_lower for p in ["notícia", "últimas notícias", "notícias de hoje", "jornal"]):
            noticias = ultimas_noticias()
            if noticias:
                return noticias
            else:
                falar("Não consegui obter notícias.")
                return "Erro: notícias não disponíveis"

        else:
            falar("Não entendi o que você disse.")
            return "Comando não reconhecido"

    except sr.UnknownValueError:
        falar("Não consegui entender o que você disse.")
        return "Erro: fala não reconhecida"

    except sr.RequestError as e:
        falar("Erro ao se conectar ao serviço de reconhecimento de voz.")
        return f"Erro: {e}"

    except OSError as e:
        falar("Erro ao acessar o microfone.")
        return f"Erro de microfone: {e}"
