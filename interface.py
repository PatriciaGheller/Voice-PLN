import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QTextEdit, QLabel, QStatusBar
from PyQt5.QtGui import QIcon
from feedback import mensagem_boas_vindas

class VoicePLNApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # Configurações da janela
        self.setWindowTitle("Voice-PLN Assistente")
        self.setGeometry(200, 200, 500, 400)

        # Layout principal
        layout = QVBoxLayout()

        # Mensagem de boas-vindas
        mensagem_boas_vindas()

        # Botão iniciar/parar
        self.btn_iniciar = QPushButton("🎤 Iniciar Captura de Voz")
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

        # Ícones (exemplo: Excel)
        self.btn_excel = QPushButton("Abrir Excel")
        self.btn_excel.setIcon(QIcon("assets/excel.png"))
        layout.addWidget(self.btn_excel)

        # Define layout
        self.setLayout(layout)

    def iniciar_captura(self):
        # Aqui futuramente chamaremos reconhecimento.py
        self.status_bar.showMessage("🎤 Ouvindo...")
        self.text_area.append("Simulação: Você disse 'Abrir Excel'")
        self.status_bar.showMessage("✅ Comando executado")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    janela = VoicePLNApp()
    janela.show()
    sys.exit(app.exec_())
