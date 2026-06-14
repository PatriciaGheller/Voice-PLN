from reconhecimento import ouvir_microfone

def main():
    print("=== Voice-PLN iniciado ===")
    print("Fale um comando...")

    while True:
        if ouvir_microfone():
            break

    print("Sistema encerrado.")

if __name__ == "__main__":
    main()
