"""
Given a string s representing a valid expression, 
implement a basic calculator to evaluate it, 
and return the result of the evaluation.

Note: You are not allowed to use any built-in 
function which evaluates strings as mathematical 
expressions, such as eval().

Constraints:
1 <= s.length <= 3 * 105
s consists of digits, '+', '-', '(', ')', and ' '.
s represents a valid expression.
'+' is not used as a unary operation (i.e., "+1" and "+(2 + 3)" is invalid).
'-' could be used as a unary operation (i.e., "-1" and "-(2 + 3)" is valid).
There will be no two consecutive operators in the input.
Every number and running calculation will fit in a signed 32-bit integer.

Ou seja, leia a string, se numeros consecutivos,a amarzene em num1[], ignore (, ,) e calcule se + ou -, 
depois numeros consecutivos,a amarzene em num2[]
"""
import re
def calculate(self, s):
# Inicialização de variáveis
    stack = []  # Stack para manter os operadores e operandos
    num = 0     # Variável para acumular o número atual
    sign = 1    # Sinal do número atual (1 para positivo, -1 para negativo)
    result = 0  # Resultado da expressão

    # Iteração através de cada caractere na string
    for char in s:
        if char.isdigit():
            # Se o caractere é um dígito, acumulamos o número
            num = num * 10 + int(char)
        elif char == '+':
            # Se encontramos um operador de adição, atualizamos o resultado
            # com o número acumulado, resetamos o número e atualizamos o sinal
            result += sign * num
            num = 0
            sign = 1
        elif char == '-':
            # Se encontramos um operador de subtração, fazemos o mesmo que o de adição,
            # mas atualizamos o sinal para negativo
            result += sign * num
            num = 0
            sign = -1
        elif char == '(':
            # Se encontramos um parêntese de abertura, empilhamos o resultado acumulado
            # e o sinal atual, resetamos o resultado e o sinal
            stack.append(result)
            stack.append(sign)
            result = 0
            sign = 1
        elif char == ')':
            # Se encontramos um parêntese de fechamento, atualizamos o resultado com o
            # número acumulado, resetamos o número, recuperamos o sinal e o resultado
            # da pilha e atualizamos o resultado acumulado
            result += sign * num
            num = 0
            result *= stack.pop()  # Recupera o sinal
            result += stack.pop()  # Recupera o resultado acumulado

    # Retorna o resultado final da expressão
    return result + sign * num

calculate(0,"(1+(4+5+2)-3)+(6-8)")