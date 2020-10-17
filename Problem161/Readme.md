# Problem #161

***English Question***

Given a 32-bit integer, return the number with is bits reversed

For example, given the binary number 

1111 0000 1111 0000 1111 0000 1111 0000

should return 

0000 1111 0000 1111 0000 1111 0000 1111

***Portuguese Question***

*Tendo um numero binário de 32bits, retorne o número com os bits invertidos,* 

*por exemplo, passado o numero abaixo*

1111 0000 1111 0000 1111 0000 1111 0000

*deverá retornar*

0000 1111 0000 1111 0000 1111 0000 1111

# Código em Python

```python
StrToTuple = lambda binaryString: tuple(x for x in binaryString)

def reverseBinary(bList: tuple):
    if (1 == len(bList)):
        if ('1' == bList[0]):
            return '0'
        return '1'
    if ('1' == bList[0]):
        return '0'+str(reverseBinary(bList[1:]))
    return '1'+str(reverseBinary(bList[1:]))

bStr = "11110000111100001111000011110000"
rbStr = reverseBinary(StrToTuple(bStr))
print(rbStr)
```

1. Transforma a **string** de um numero binário qualquer em uma **Tupla**, para garantir que a função trabalhe com os valores sem altera-los 
2. Chama a função **reverseBinary** passando a Tupla gerada como parâmetro
3. Dentro da função é verificado a quantidade de caracteres, caso só tenha um caractere ela o inverte, caso contrário inverte o primeiro caractere da **Tupla** e concatena com o inverso da cauda. Para gerar o inverso da cauda da **Tupla** a mesma é passada como parâmetro para a função **reverseBinary,** tendo assim uma função recursiva para inverter o codigo binario de um numero