# menu de opcoes para os operadores selecionaveis
def mostrar_menu():
    print("===================")
    print("    CALCULADORA    ")
    print("===================")
    print("\n")
    print("1 - Soma")
    print("2 - Subtracao")
    print("3 - Multiplicacao")
    print("4 - Divisao")
    print("0 - SAIR")

def ler_operacao():
    op = input("Selecione uma das opcoes para continuar (Digite apenas o numero da opcao): ")
    return op

# organizacao do projeto, ordem em que inicia
def main():
    mostrar_menu()
    opcao_operador = ler_operacao()
    print(f"voce escolheu a opcao: {opcao_operador}")
    

if __name__ == "__main__":
    main()