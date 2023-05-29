from automatos_analizador_lexico import identificadores, palavras_reservadas, numeros, comentarios, simbolos_especiais


def lexico(nome_arquivo):

    with open(nome_arquivo, "r", encoding='utf') as arquivo:
        texto = arquivo.read()
        while (texto):
            token = ''
            if texto[0] in ('\t', '\n', ' '):
                texto = texto[1:]
            elif identificadores(texto):
                token = identificadores(texto)
                print('Identificador: '+token)
                texto = texto[len(token):]
            elif comentarios(texto):
                token = comentarios(texto)
                print('Comentarios: '+token)
                texto = texto[len(token):]
            elif numeros(texto):
                token = numeros(texto)
                print('Digito: ' + token)
                texto = texto[len(token):]
            elif simbolos_especiais(texto):
                token = simbolos_especiais(texto)
                print('simbolo especial: ' + token)
                texto = texto[len(token):]
            else:
                print('Invalidos: '+texto[0])
                texto = texto[1:]


lexico("arquivo.txt")
