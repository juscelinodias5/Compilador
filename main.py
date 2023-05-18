from automatos_analizador_lexico import identificadores, palavras_reservadas, numeros, comentarios, simbolos_especiais


def ler_arquivo(nome_arquivo):
    with open(nome_arquivo, "r", encoding='utf') as arquivo:
        palavra = arquivo.read()
        


ler_arquivo("arquivo.txt")
