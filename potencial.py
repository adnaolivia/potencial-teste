import tkinter.simpledialog as simpledialog
import tkinter.messagebox as messagebox
import tkinter as tk

def main():
    # Inicializa a janela principal
    root = tk.Tk()
    root.withdraw()  # Oculta a janela principal

    # Solicita ao usuário a base e o expoente
    PrimeiroNumero = simpledialog.askstring("Entrada", "Entre com a base:")
    SegundoNumero = simpledialog.askstring("Entrada", "Entre com o expoente:")

    # Converte os valores para float
    Base = float(PrimeiroNumero)
    Expoente = float(SegundoNumero)

    # Verifica se o expoente é negativo
    if Expoente < 0:
        Potencial = 0 - Expoente
    else:
        Potencial = Expoente

    # Calcula a potência
    Resultado = 1
    while Potencial != 0:
        Resultado = Resultado * Base
        Potencial = Potencial - 1

    # Se o expoente for negativo e a base for diferente de zero
    if Expoente < 0 and Base != 0:
        Resultado = 1 / Resultado
    elif Base == 0:
        messagebox.showinfo("Resultado", "A potência é um valor finito")

    # Exibe o resultado
    messagebox.showinfo("Resultado", f"A potência é {Resultado}")

    # Finaliza o programa
    root.quit()

if __name__ == "__main__":
    main()
