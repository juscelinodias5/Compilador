from automatos_analizador_lexico import identificadores, palavras_reservadas, numeros, comentarios, simbolos_especiais


def lexico(nome_arquivo):

    with open(nome_arquivo, "r", encoding='utf') as arquivo:
        palavra = arquivo.read()
        while (palavra):
            token = ''
            if identificadores(palavra):
                token = identificadores(palavra)
                print('Identificador: '+token)
                palavra = palavra[len(token):]
            elif comentarios(palavra):
                token = comentarios(palavra)
                print('Comentarios: '+token)
                palavra = palavra[len(token):]
            elif numeros(palavra):
                token = numeros(palavra)
                print('Digitos: ' + token)
                palavra = palavra[len(token):]
            elif simbolos_especiais(palavra):
                token = simbolos_especiais(palavra)
                print('simbolo especial: ' + token)
                palavra = palavra[len(token):]
            else:
                palavra = palavra[1:]


list_identif = []
lexico("arquivo.txt")
