import re

def calcular():
    print('''Olá! Eu sou a calculadora de fita! Para começar, basta digitar o número ou operação que você deseja.
             Operações válidas:
             + -> Soma
            - -> Subtração
            * -> Multiplicação
            / -> Divisão
            = -> Conclusão
            c -> Limpar
            ''')
    concluido = False
    resultado = 0
    operador = None
    num1 = 0
    num2 = 0
    while not concluido:
        entrada = input('Por favor digite o número ou a operação desejada: ')
        try:
            num = float(entrada)
            if operador:
                num2 = num
            else:
                num1 = num
            prompt = num
        except ValueError:
            if not re.match('^[*+\-/c=]$', entrada):
                prompt = 'Não reconheci o que você digitou! Por favor digite apenas números ou operadores válidos'
            else:
                if entrada == '=':
                    if operador:
                        concluido = True
                        resultado = eval(f'{num1} {operador} {num2}')
                        print_apagando_linha('='*10, True)
                        prompt = f'{num1} {operador} {num2} = {resultado}'
                    else:
                        prompt = 'Você digitou o caractere de conclusão de cálculo, mas você não informou qual operação deseja fazer!'
                elif entrada == 'c':
                    num1 = 0
                    num2 = 0
                    operador = None
                else:
                    operador = entrada
                    prompt = entrada

        print_apagando_linha(prompt)
    return resultado


def print_apagando_linha(prompt, nova_linha=False):
    apagar_linha_acima()
    print(prompt)
    if nova_linha:
        print()


def apagar_linha_acima():
    LINHA_ACIMA = '\033[1A'
    LIMPAR_LINHA = '\x1b[2K'
    print(LINHA_ACIMA, end=LIMPAR_LINHA)


if __name__ == '__main__':
    calcular()
