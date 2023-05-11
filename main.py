import re

#TODO mensagem de boas vindas informando os operadores válidos
'''
+ -> Soma
- -> Subtração
* -> Multiplicação
/ -> Divisão
= -> Conclusão
'''
def calcular():
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
            #TODO incluir regex para validar operadores, se falhar, notifica usuário, senão armazena e exibe o prompt abaixo.
            prompt = 'não reconheci o que você digitou! Por favor digite apenas números ou operadores válidos'
            if entrada == '=':
                if operador:
                    concluido = True
                    resultado = eval(f'{num1} {operador} {num2}')
                    print_apagando_linha('-'*10, True)
                    prompt = f'{num1} {operador} {num2} = {resultado}'
                else:
                    prompt = 'Você digitou o caractere de conclusão de cálculo, mas você não informou qual operação deseja fazer!'
            else:
                operador = entrada
                prompt = entrada
            
        print_apagando_linha(prompt)
    return resultado

def print_apagando_linha(prompt, nova_linha=False):
    print(f'\033[1A {prompt} \033[K')
    if nova_linha:
        print('\n')

if __name__ == '__main__':
    calcular()