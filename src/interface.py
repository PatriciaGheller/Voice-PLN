import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QTextEdit, QStatusBar
from PyQt5.QtGui import QIcon
from src.feedback import mensagem_boas_vindas
from src.reconhecimento import ouvir_microfone
from src.apis import previsao_tempo, tocar_playlist, ultimas_noticias
from src.comandos import abrir_navegador, abrir_excel

class VoicePLNApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # Configurações da janela
        self.setWindowTitle("Voice-PLN Assistente")
        self.setGeometry(200, 200, 500, 500)

        # Layout principal
        layout = QVBoxLayout()

        # Mensagem de boas-vindas sonora
        mensagem_boas_vindas()

        # Botão iniciar/parar (microfone)
        self.btn_iniciar = QPushButton("Iniciar Captura de Voz")
        self.btn_iniciar.setIcon(QIcon("assets/icons/microfone.png"))
        self.btn_iniciar.clicked.connect(self.iniciar_captura)
        layout.addWidget(self.btn_iniciar)

        # Área de texto para mostrar comandos reconhecidos
        self.text_area = QTextEdit()
        self.text_area.setPlaceholderText("Aqui aparecerá o que você disse...")
        layout.addWidget(self.text_area)

        # Barra de status
        self.status_bar = QStatusBar()
        self.status_bar.showMessage("✅ Voice-PLN pronto para ouvir")
        layout.addWidget(self.status_bar)

        # Botões adicionais com ícones e funções
        self.btn_clima = QPushButton("Previsão do Tempo")
        self.btn_clima.setIcon(QIcon("assets/icons/clima.png"))
        self.btn_clima.clicked.connect(lambda: self.executar_funcao(previsao_tempo))
        layout.addWidget(self.btn_clima)

        self.btn_noticias = QPushButton("Últimas Notícias")
        self.btn_noticias.setIcon(QIcon("assets/icons/noticias.png"))
        self.btn_noticias.clicked.connect(lambda: self.executar_funcao(ultimas_noticias))
        layout.addWidget(self.btn_noticias)

        self.btn_musica = QPushButton("Tocar Música")
        self.btn_musica.setIcon(QIcon("assets/icons/musica.png"))
        self.btn_musica.clicked.connect(lambda: self.executar_funcao(tocar_playlist))
        layout.addWidget(self.btn_musica)

        self.btn_navegador = QPushButton("Abrir Navegador")
        self.btn_navegador.setIcon(QIcon("assets/icons/navegador.png"))
        self.btn_navegador.clicked.connect(lambda: self.executar_funcao(abrir_navegador))
        layout.addWidget(self.btn_navegador)

        self.btn_excel = QPushButton("Abrir Excel")
        self.btn_excel.setIcon(QIcon("assets/icons/excel.png"))
        self.btn_excel.clicked.connect(lambda: self.executar_funcao(abrir_excel))
        layout.addWidget(self.btn_excel)

        # Define layout
        self.setLayout(layout)

    def iniciar_captura(self):
        self.status_bar.showMessage("🎤 Ouvindo...")
        reconhecido = ouvir_microfone()  # Chama reconhecimento.py
        if reconhecido:
            self.text_area.append(f"Você disse: {reconhecido}")
            self.status_bar.showMessage("✅ Comando executado")
        else:
            self.text_area.append("Não entendi o que você disse.")
            self.status_bar.showMessage("⚠️ Tente novamente")

    def executar_funcao(self, funcao):
        """Executa uma função e mostra o resultado na área de texto"""
        try:
            resultado = funcao()
            if resultado:
                self.text_area.append(str(resultado))
            self.status_bar.showMessage("✅ Comando executado")
        except Exception as e:
            print("Erro capturado:", e)
            self.text_area.append(f"Erro: {e}")
            self.status_bar.showMessage("⚠️ Falha ao executar comando")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    janela = VoicePLNApp()
    janela.show()
    sys.exit(app.exec_())
