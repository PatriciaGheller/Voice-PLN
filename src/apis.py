import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from src.feedback import falar

# ==========================
# API de Clima (OpenWeather)
# ==========================
def previsao_tempo(cidade="Vila Valério"):
    chave_api = "SUA_CHAVE_OPENWEATHER"
    url = f"http://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={chave_api}&lang=pt_br&units=metric"
    resposta = requests.get(url).json()
    clima = resposta["weather"][0]["description"]
    temp = resposta["main"]["temp"]
    falar(f"A previsão para {cidade} é de {clima}, com temperatura de {temp} graus Celsius.")
    return f"{cidade}: {clima}, {temp}°C"

# ==========================
# API de Música (Spotify)
# ==========================
def tocar_playlist():
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
        client_id="SEU_CLIENT_ID",
        client_secret="SEU_CLIENT_SECRET",
        redirect_uri="http://localhost:8888/callback",
        scope="user-modify-playback-state"
    ))
    playlist_uri = "spotify:playlist:SUA_PLAYLIST_ID"
    sp.start_playback(context_uri=playlist_uri)
    falar("Tocando sua playlist favorita no Spotify.")
    return "Spotify: Playlist iniciada"

# ==========================
# API de Notícias (NewsAPI)
# ==========================
def ultimas_noticias():
    chave_api = "SUA_CHAVE_NEWSAPI"
    url = f"https://newsapi.org/v2/top-headlines?country=br&apiKey={chave_api}"
    resposta = requests.get(url).json()
    artigos = resposta["articles"][:3]
    titulos = []
    for noticia in artigos:
        titulos.append(noticia['title'])
        falar(f"Notícia: {noticia['title']}")
    return titulos
