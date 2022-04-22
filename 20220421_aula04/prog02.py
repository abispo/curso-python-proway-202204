# Manipulação de arquivos txt
# Escrita

if __name__ == '__main__':

    # Quando abrimos o arquivo no modo w (escrita), se o arquivo
    # não existir, ele é criado, e se existir, o seu conteúdo é
    # truncado (sobrescrito)
    with open("emails.txt", mode="w") as _file:
        # O método write() escreve no arquivo
        _file.write("juliana@email.com\n")

        # O método writelines escreve os itens da lista no arquivo
        _file.writelines([
            "jessica@email.com\n",
            "lais@email.com\n",
            "ursula@email.com\n"
        ])

    # Quando abrimos o arquivo no modo a (append), se o arquivo
    # não existir, ele é criado, e se existir, o conteúdo escrito
    # é adicionado no final do arquivo
    with open("telefones.txt", mode="a") as _file:
        _file.write("+5547945629875\n")
        _file.writelines([
            "+5547998726354\n",
            "+55987111123\n"
        ])
