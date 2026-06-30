import sys
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

def somar(numero1,numero2):
    return numero1+numero2

def subtrair(numero1,numero2):
    return numero1-numero2

def multiplicar(numero1,numero2):
    return numero1*numero2

def dividir(numero1,numero2):
    if numero2 != 0:
        return numero1/numero2

def ler_numero():
    return float(input("Selecione um numero: "))

# organizacao do projeto, ordem em que inicia
def main():
    mostrar_menu()
    operador = ler_operacao()

    if operador == "0":
        print("\n")
        print("voce saiu!")
        sys.exit(0)

    print(f"voce escolheu a opcao: {operador}")

    numero1 = ler_numero()
    numero2 = ler_numero()

    if operador == "1":
        soma = somar(numero1,numero2)
        print(f"{numero1} + {numero2} = {soma}")

    elif operador == "2":
        subtracao = subtrair(numero1,numero2)
        print(f"{numero1} - {numero2} = {subtracao}")

    elif operador == "3":
        multiplicacao = multiplicar(numero1,numero2)
        print(f"{numero1} * {numero2} = {multiplicacao}")

    elif operador == "4":
        if numero2 != 0:
            divisao = dividir(numero1,numero2)
            print(f"{numero1} / {numero2} = {divisao}")
        else:
            print("Divisão por zero nao é permitida")
    
if __name__ == "__main__":
    main()