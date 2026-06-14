from reconhecimento import ouvir_microfone
from feedback import mensagem_boas_vindas

def main():
    mensagem_boas_vindas()
    print("=== Voice-PLN iniciado ===")
    print("Fale um comando...")

    while True:
        if ouvir_microfone():
            break

    print("Sistema encerrado.")

if __name__ == "__main__":
    main()
