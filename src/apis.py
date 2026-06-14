import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from src.feedback import falar
import os
from dotenv import load_dotenv

load_dotenv()  # carrega variáveis do .env

# ==========================
# API de Clima (OpenWeather)
# ==========================
def previsao_tempo(cidade="Vila Valério"):
    chave_api = os.getenv("OPENWEATHER_KEY")  # pega do .env
    url = f"http://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={chave_api}&lang=pt_br&units=metric"
    resposta = requests.get(url).json()

    if "weather" in resposta and "main" in resposta:
        clima = resposta["weather"][0]["description"]
        temp = resposta["main"]["temp"]
        falar(f"A previsão para {cidade} é de {clima}, com temperatura de {temp} graus Celsius.")
        return f"{cidade}: {clima}, {temp}°C"
    else:
        return "Não foi possível obter a previsão do tempo."

# Função auxiliar para extrair cidade da frase
def extrair_cidade(frase):
    palavras = frase.split()
    # procura "em", "no" ou "na" e pega o que vem depois
    for preposicao in ["em", "no", "na"]:
        if preposicao in palavras:
            indice = palavras.index(preposicao)
            cidade = " ".join(palavras[indice+1:])
            return cidade
    return None

# Função que integra fala com previsão
def previsao_tempo_por_fala(frase):
    cidade = extrair_cidade(frase)
    if cidade:
        return previsao_tempo(cidade)
    else:
        return previsao_tempo()  # usa padrão se não encontrar cidade

# ==========================
# API de Música (Spotify)
# ==========================
def tocar_playlist():
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
        client_id=os.getenv("SPOTIFY_CLIENT_ID"),
        client_secret=os.getenv("SPOTIFY_CLIENT_SECRET"),
        redirect_uri="http://localhost:8888/callback",
        scope="user-modify-playback-state"
    ))
    playlist_uri = f"spotify:playlist:{os.getenv('SPOTIFY_PLAYLIST_ID')}"
    sp.start_playback(context_uri=playlist_uri)
    falar("Tocando sua playlist favorita no Spotify.")
    return "Spotify: Playlist iniciada"

# ==========================
# API de Notícias (NewsAPI)
# ==========================
def ultimas_noticias():
    chave_api = os.getenv("NEWSAPI_KEY")
    url = f"https://newsapi.org/v2/top-headlines?country=br&apiKey={chave_api}"
    resposta = requests.get(url).json()

    if "articles" in resposta:
        artigos = resposta["articles"][:3]
        titulos = []
        for noticia in artigos:
            titulo = noticia.get("title", "Sem título")
            titulos.append(titulo)
            falar(f"Notícia: {titulo}")
        return titulos
    else:
        return ["Não foi possível obter as últimas notícias."]