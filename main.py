from automatos_analizador_lexico import identificadores, palavras_reservadas, numeros, comentarios, simbolos_especiais


def ler_arquivo(nome_arquivo):
    token = ''

    with open(nome_arquivo, "r", encoding='utf') as arquivo:
        palavra = arquivo.read()
        while palavra:
            if identificadores(palavra):
                token = identificadores(palavra)
                # list_identif.append(token)
                print('Identificador: '+token)
                palavra = palavra[len(token):]
            else:
                palavra = palavra[1:]


list_identif = []
ler_arquivo("arquivo.txt")
# print(list_identif)
