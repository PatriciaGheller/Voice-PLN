# Voice-PLN 🎤🤖

O **Voice-PLN** é um assistente de voz em Python que utiliza **Processamento de Linguagem Natural (PLN)** para reconhecer comandos falados e executar ações no computador.  
Ele combina **SpeechRecognition**, **PyQt5** para interface gráfica, e integrações com **APIs externas** (clima, Spotify e notícias), tornando-se um sistema multimídia interativo e divertido.

---

## 🚀 Funcionalidades
- Reconhecimento de voz em português (via Google SpeechRecognition).
- Execução de comandos locais:
  - Abrir navegador Chrome
  - Abrir Excel
  - Abrir PowerPoint
  - Abrir Microsoft Edge
- Integrações externas:
  - 🌦️ **Clima**: previsão do tempo via OpenWeatherMap, com suporte a frases naturais (“em”, “no”, “na”).
  - 🎵 **Música**: tocar playlists no Spotify.
  - 📰 **Notícias**: últimas manchetes via NewsAPI.
- Interface gráfica moderna com **PyQt5**:
  - Botão para iniciar/parar captura de voz.
  - Área de texto exibindo o que foi reconhecido.
  - Barra de status com mensagens dinâmicas.
  - Ícones (armazenados na pasta `assets/`) para cada comando.
- Feedback sonoro com **pyttsx3:**
  - mensagens de boas-vindas e confirmações.
  - Voz personalizada (masculina/feminina).
  - Ajuste de velocidade e volume.
  - Seleção automática de voz em português Brasil, se disponível.


## 🔎 Como cada botão funciona

- 🎤 Microfone → `inicia a captura de voz` e mostra o que você disse.

- 🌦️ Clima → `chama previsao_tempo()` e mostra o resultado.

- 📰 Notícias → `chama ultimas_noticias()` e exibe as manchetes.

- 🎵 Música → `chama tocar_playlist()` e inicia sua playlist.

- 🌐 Navegador → `chama abrir_navegador()` e abre o browser.

- 📊 Excel → `chama abrir_excel()` e abre o Excel.


---

## 📂 Estrutura do Projeto

Voice-PLN/
│
├── assets/              # Ícones e recursos visuais
├── src/                 # Código-fonte principal
│   ├── __init__.py      # Torna src um pacote Python
│   ├── feedback.py      # Funções de voz e mensagens sonoras
│   ├── comandos.py      # Comandos locais (abrir apps)
│   ├── reconhecimento.py# Captura e interpretação da fala
│   ├── apis.py          # Integrações externas (clima, Spotify, notícias)
│   ├── interface.py     # Interface gráfica em PyQt5
│   └── main.py          # Ponto de entrada principal
├── requirements.txt     # Dependências do projeto
├── .gitignore           # Arquivos ignorados pelo Git
└── README.md            # Documentação
  


---

## 🔧 Instalação

1. Clone o repositório:
   ```bash
   git clone https://github.com/PatriciaGheller/Voice-PLN.git
   cd Voice-PLN

2. Crie um ambiente virtual (opcional, mas recomendado):

python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows

3. Instale as dependências:

pip install -r requirements.txt

### 📌 Dependências principais:

- speechrecognition

- pyttsx3

- PyQt5

- requests

- spotipy

## ⚙️ Configuração das APIs

 - `OpenWeatherMap:` crie uma conta e obtenha sua chave em https://openweathermap.org/api.

- `Spotify:` registre um app em https://developer.spotify.com e configure client_id, `client_secret` e `redirect_uri`.

- `NewsAPI:` obtenha sua chave em https://newsapi.org.

- Configure todas as chaves no arquivo `.env`.

## ▶️ Como usar

1.Execute a interface gráfica:

`python interface.py`

2. Clique em 🎤 Iniciar Captura de Voz e fale um comando:

- “Abrir Excel”

- “Abrir navegador”

- “Qual a previsão do tempo no Rio de Janeiro?”

- “Quais são as últimas notícias?”

- “Tocar minha playlist favorita”

3. O resultado aparecerá na área de texto e será falado pelo sistema.

## ▶️ Como rodar

Para iniciar o projeto completo (com mensagem de boas-vindas e carregamento modular):

`python -m src.main`


## 🎉 Mensagem de boas-vindas

Ao iniciar, o sistema fala:

`"Bem-vindo ao Voice-PLN! Seu assistente de voz está pronto para ajudar."`

## 📌 Próximos Passos

- Melhorar integração com mais APIs (ex.: tradutor, calendário, e-mail).

- Criar versão mobile com Kivy.

- Adicionar suporte a múltiplos idiomas.


`Projeto aberto para melhorias, seja bem-vindo para contribuir.`🎯

## 👩‍💻 Autora

Projeto desenvolvido por Patrícia Gheller.



