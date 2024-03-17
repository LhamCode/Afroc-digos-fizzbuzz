divisores = [3, 5]
palavras = ["FIZZ", "BUZZ"]
numero = int(input("Entre com um número: "))

for i in range(1, numero + 1):
    saida = ""
    for j in range(len(divisores)):
        if i % divisores[j] == 0:
            saida += palavras[j]
    if saida == "":
        print(i)
    else:
        print(saida)

    # divisores = [3, 5]: Aqui, definimos uma lista divisores que contém os números pelos quais vamos verificar se o número atual é divisível. No caso do clássico problema FizzBuzz, usamos 3 e 5.

    # palavras = ["FIZZ", "BUZZ"]: Aqui, definimos uma lista palavras que contém as palavras que queremos imprimir quando o número atual for divisível pelos números correspondentes na lista divisores. No caso do FizzBuzz, usamos "FIZZ" e "BUZZ".

    # numero = int(input("Entre com um número: ")): Solicita ao usuário que insira um número inteiro e armazena o valor fornecido na variável numero.

    # for i in range(1, numero + 1):: Este é um loop que percorre todos os números de 1 até o número fornecido pelo usuário (incluindo o próprio número fornecido).

    # saida = "": Para cada número no loop externo, criamos uma string vazia saida que será usada para armazenar as palavras "FIZZ", "BUZZ" ou "FIZZBUZZ" conforme necessário.

    # for j in range(len(divisores)):: Este é um loop interno que percorre os índices da lista divisores.

    # if i % divisores[j] == 0:: Aqui, verificamos se o número atual (i) é divisível pelo divisor correspondente (divisores[j]). Se o resto da divisão for zero, significa que i é divisível por divisores[j].

    # saida += palavras[j]: Se i for divisível por divisores[j], adicionamos a palavra correspondente (palavras[j]) à string saida.

    # if saida == "":: Após o loop interno, verificamos se a saida ainda está vazia. Se estiver, significa que o número atual não é divisível por nenhum dos divisores (3 ou 5 no caso do FizzBuzz).

    # print(i): Se saida estiver vazia, simplesmente imprimimos o número i.

    # else:: Se a saida não estiver vazia, isso significa que o número é divisível por 3, 5 ou ambos.

    # print(saida): Nesse caso, imprimimos a saida, que pode ser "FIZZ", "BUZZ" ou "FIZZBUZZ", dependendo de quais divisores i é divisível.