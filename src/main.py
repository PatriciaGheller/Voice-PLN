import sys
from PyQt5.QtWidgets import QApplication
from src.interface import VoicePLNApp
from src.feedback import mensagem_boas_vindas

def main():
    try:
        # Exibe mensagem inicial de boas-vindas em voz
        mensagem_boas_vindas()
    except Exception as e:
        print("Erro na mensagem de boas-vindas:", e)

    try:
        # Inicializa a aplicação gráfica
        app = QApplication(sys.argv)
        janela = VoicePLNApp()
        janela.show()

        # Mantém o loop da aplicação até o usuário fechar
        sys.exit(app.exec_())
    except Exception as e:
        print("Erro ao iniciar a aplicação:", e)

if __name__ == "__main__":
    main()
