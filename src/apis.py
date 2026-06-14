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
    chave_api = os.getenv("OPENWEATHER_KEY")
    if not chave_api:
        erro = "Chave da API OpenWeather não encontrada no .env."
        falar(erro)
        return erro

    url = f"http://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={chave_api}&lang=pt_br&units=metric"
    resposta = requests.get(url).json()

    if resposta.get("cod") == 200:
        clima = resposta["weather"][0]["description"]
        temp = resposta["main"]["temp"]
        mensagem = f"{cidade}: {clima}, {temp}°C"
        falar(f"A previsão para {cidade} é de {clima}, com temperatura de {temp} graus Celsius.")
        return mensagem
    else:
        erro = f"Não foi possível obter a previsão do tempo: {resposta.get('message', 'Erro desconhecido')}"
        falar(erro)
        return erro

# Função auxiliar para extrair cidade da frase
def extrair_cidade(frase):
    palavras = frase.split()
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
        return previsao_tempo()

# ==========================
# API de Música (Spotify)
# ==========================
def tocar_playlist():
    try:
        sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
            client_id=os.getenv("SPOTIFY_CLIENT_ID"),
            client_secret=os.getenv("SPOTIFY_CLIENT_SECRET"),
            redirect_uri="http://127.0.0.1:8888/callback",
            scope="user-modify-playback-state"
        ))
        playlist_id = os.getenv("SPOTIFY_PLAYLIST_ID")
        if not playlist_id:
            erro = "ID da playlist não configurado no .env."
            falar(erro)
            return erro

        playlist_uri = f"spotify:playlist:{playlist_id}"
        sp.start_playback(context_uri=playlist_uri)
        falar("Tocando sua playlist favorita no Spotify.")
        return "Spotify: Playlist iniciada"
    except Exception as e:
        erro = f"Erro ao tocar playlist: {e}"
        falar(erro)
        return erro

# ==========================
# API de Notícias (NewsAPI)
# ==========================
def ultimas_noticias():
    chave_api = os.getenv("NEWSAPI_KEY")
    if not chave_api:
        erro = "Chave da API NewsAPI não encontrada no .env."
        falar(erro)
        return erro

    # Se for Brasil, usa busca por palavra-chave
    url = f"https://newsapi.org/v2/everything?q=Brasil&language=pt&apiKey={chave_api}"
    resposta = requests.get(url).json()

    if resposta.get("status") == "ok" and "articles" in resposta:
        artigos = resposta.get("articles", [])[:5]
        if not artigos:
            erro = "Nenhuma notícia disponível no momento."
            falar(erro)
            return erro

        titulos = [art.get("title", "Sem título") for art in artigos]

        # Áudio: fala só o primeiro título
        primeiro_titulo = titulos[0]
        falar(f"Última notícia: {primeiro_titulo}")

        # Texto: retorna todos os títulos separados por linha
        return "\n".join(titulos)

    elif resposta.get("status") == "error":
        erro = f"Erro da NewsAPI: {resposta.get('code', '')} - {resposta.get('message', 'Mensagem não informada')}"
        falar("Erro ao buscar notícias.")
        return erro

    else:
        erro = "Não foi possível obter as últimas notícias (resposta inesperada)."
        falar(erro)
        return erro
