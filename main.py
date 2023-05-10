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
        entrada = input('Por favor digite o número ou a operação desejada')
        try:
            num = float(entrada)
            if operador:
                num2 = num
            else:
                num1 = num
            output = num
        except ValueError:
            output = entrada
            #TODO incluir regex para validar operadores, se falhar, notifica usuário, senão armazena e registra no terminal
            output = 'não reconheci o que você digitou! Por favor digite apenas números ou operadores válidos'
            operador = entrada
            #TODO se for adicionado operador de conclusão, então executar o cálculo e registrar o resultado 
            
        print(output)
    return resultado

if __name__ == '__main__':
    calcular