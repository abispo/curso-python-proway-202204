"""
Exercício
---------

Criar um algoritmo que calcula a média de notas de um aluno e mostra uma mensagem, de
acordo com a média final.
Se a média for menor que 5:
    Mostrar a mensagem "Aluno reprovado"
Se a média for maior ou igual a 5 E menor do que 7:
    Mostrar a mensagem "Aluno em recuperação".
Se a média for maior do que 7:
    Mostrar a mensagem "Aluno aprovado".

&&  -> and
||  -> or
!   -> not

"""

if __name__ == '__main__':

    n1 = float(input("Informe a primeira nota: "))
    n2 = float(input("Informe a segunda nota: "))
    n3 = float(input("Informe a terceira nota: "))

    media = (n1 + n2 + n3) / 3  # O '/' tem precedência sobre o '+'

    # Podemos formatar a quantidade de casas decimais mostradas depois do ponto
    print(f"Sua média é {media:.2f}")

    if media < 5:
        print("Aluno reprovado!")

    elif media >= 5 and media < 7:
        print("Aluno em Recuperação!")

    else:
        print("Aluno aprovado!")