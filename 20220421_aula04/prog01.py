# Manipulação de arquivos txt
# Leitura

if __name__ == '__main__':

    # Utilizamos a função built-in open() para abrir um arquivo.

    # O primeiro argumento é o nome completo do arquivo que vamos
    # abrir (obrigatório)

    """
    https://www.w3schools.com/python/python_file_handling.asp
    r - Read - Default value. Opens a file for reading, error if the file does not exist
    a - Append - Opens a file for appending, creates the file if it does not exist
    w - Write - Opens a file for writing, creates the file if it does not exist
    x - Create - Creates the specified file, returns an error if the file exists
    
    """
    _file = open(file="clientes.txt", mode="r")

    # O método tell() retorna a posição atual do cursor
    print(f"Posição do cursor: {_file.tell()}")

    # read(), readline(), readlines()

    # read() é o método que retorna todo o conteúdo do arquivo
    content = _file.read()

    # O método read(), como lê o arquivo inteiro, joga o cursor
    # para o final
    print(f"Posição do cursor: {_file.tell()}")


    # Imprimir no terminal o tipo da variável content
    print(type(content))

    # Imprime o conteúdo do arquivo
    print(content)

    # O método readline() lê uma linha do arquivo
    # readline() possui o argumento opcional __limit, onde podemos
    # limitar a quantidade de caracteres retornados.

    # ps: a linha abaixo não retorna nada
    print(_file.readline())

    # Não retorna nada pois o cursor que o Python cria para ler o
    # arquivo está na posição final. Pra lermos o arquivo novamente
    # precisamos "rebobinar" o cursor para o início usando o método
    # seek

    # Mudamos o cursor para o início do arquivo
    _file.seek(0, 0)

    # Dessa maneira podemos ler o arquivo novamente
    print(_file.readline())

    # Lê a próxima linha
    print(_file.readline())

    # Podemos limitar a quantidade de caracteres lidos de uma linha
    print(_file.readline(3))

    # Voltando o cursor para o início do arquivo
    _file.seek(0)

    print(_file.readlines())

    # Sempre devemos fechar o arquivo que abrimos com open()
    _file.close()
