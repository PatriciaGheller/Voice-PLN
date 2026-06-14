import sys
from PyQt5.QtWidgets import QApplication
from src.interface import VoicePLNApp
from src.feedback import mensagem_boas_vindas

def main():
    # Exibe mensagem inicial de boas-vindas em voz
    mensagem_boas_vindas()

    # Inicializa a aplicação gráfica
    app = QApplication(sys.argv)
    janela = VoicePLNApp()
    janela.show()

    # Mantém o loop da aplicação até o usuário fechar
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
