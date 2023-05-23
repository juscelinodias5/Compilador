import string as s

LETRAS = s.ascii_letters  # todas as letras do alfabeto
DIGITOS = s.digits  # todos os digitos de 0 a 9
SIMBOLOS_ESPECIAIS = [';', ',', '.', '+', '-', '*',
                      '(', ')', '<', '>', ':', '=', '{', '}', '/', '@', '#']


# indentificadores
# EX: exemplo de alguns identificadores válidos: i , jx , z_teste , k12aa3, u_teste123 , u_12tes3, ab#sd, a9#sd
# exemplo de alguns identificadores inválidos: z_b_bb_ , hhz_nota, 2abc, #abc, asd#, W#D#Df, 2#rt,


def identificadores(palavra):
    estado = 0
    token = ''
    aux = ''  # recebe o caracter válido em um estado não final
    for simbolo in palavra:
        if estado == 0 and simbolo in LETRAS:
            estado = 1
            token += simbolo
        elif estado == 1 and (simbolo in LETRAS or simbolo in DIGITOS):
            estado = 3
            token += simbolo
        elif estado == 1 and simbolo in ('_', '#'):
            estado = 2
            aux += simbolo
        elif estado == 3 and (simbolo in LETRAS or simbolo in DIGITOS):
            estado = 3
            token += simbolo
        elif estado == 3 and simbolo == "#":
            estado = 4
            aux += simbolo
        elif estado in (2, 4, 5) and (simbolo in LETRAS or simbolo in DIGITOS):
            estado = 5
            token += aux
            aux = ''
            token += simbolo
        else:
            return token

    return token


# if __name__ == "__main__":
#     identificadores_validos = ['i', 'jx', 'z_teste',
#                                'k12aa3', 'u_teste123', 'u_12tes3', 'ab#sd', 'a9#sd']
#     identificadores_invalidos = ['z_b_bb_', 'hhz_nota',
#                                  '2abc', '#abc', 'asd#', 'W#D#Df', '2#rt']

#     for identificador in identificadores_invalidos:
#         print(identificadores(identificador))

#  Automato para Palavras reservadas
#  program, if, then, else, while, do, until, repeat, int, double, char, case, switch, end, procedure, function,
#  for, begin


def palavras_reservadas(palavra):
    estado = 0

    for simbolo in palavra:
        if estado == 0 and simbolo in LETRAS:
            estado = 1
        elif estado == 1 and simbolo == ':':
            estado = 1
        else:
            estado = None
            break

    if estado == 1:
        print("Palavra reservada")
    else:
        print("cadeia não reconhecida")


# palavra = "sasdjsd"
# palavras_reservadas(palavra)

# simbolos especiais
# ; , . + - *
# ( ) < > : =
# { } / @  #
# := <> <= >= ** ++


def simbolos_especiais(palavra):
    estado = 0
    token = ''
    for simbolo in palavra:
        if estado == 0:
            if simbolo in SIMBOLOS_ESPECIAIS:
                estado = 1
                token += simbolo
            elif simbolo in (":", ">"):
                estado = 2
                token += simbolo
            elif simbolo == "<":
                estado = 3
                token += simbolo
            elif simbolo == "*":
                estado = 4
                token += simbolo
            elif simbolo == "+":
                estado = 5
                token += simbolo
        elif estado == 2 and simbolo == '=':
            estado = 1
            token += simbolo
        elif estado == 3 and simbolo in ('=', '>'):
            estado = 1
            token += simbolo
        elif estado == 4 and simbolo == '*':
            estado = 1
            token += simbolo
        elif estado == 5 and simbolo == '+':
            estado = 1
            token += simbolo
        else:
            return token

    return token


# if __name__ == "__main__":
#     simbolos_validos = [';', ',', '.', '+', '-', '*',
#                         '(', ')', '<', '>', ':', '=', '{', '}', '/', '@', '#']
#     simbolos_invalidos = [';;', ',,', '...', '<<',
#                           '>>', '<<=', '>>=', '7', 's', '&', '%', 'wea', '//']

#     for palavra in simbolos_invalidos:
#         print(simbolos_especiais(palavra))


# Reconhecer e tratar comentários:
# Para uma linha: @ @, # # Para várias linhas : inicio // fim: //

def comentarios(palavra):
    estado = 0
    token = ''
    for simbolo in palavra:
        if estado == 0:
            if simbolo == "#":
                estado = 3
                token += simbolo
            elif simbolo == "@":
                estado = 1
                token += simbolo
            elif simbolo == "/":
                estado = 6
                token += simbolo
            else:
                return
        elif estado == 1 and simbolo == "@":
            estado = 2
            token += simbolo
        elif estado == 2:
            if simbolo == '\n':
                token += simbolo
                return token
            else:
                estado = 2
                token += simbolo
        elif estado == 3 and simbolo == "#":
            estado = 4
            token += simbolo
        elif estado == 4:
            if simbolo == "#":
                estado = 5
                token += simbolo
            else:
                estado = 4
                token += simbolo
        elif estado == 5:
            if simbolo == "#":
                token += simbolo
                return token
            else:
                estado = 4
                token += simbolo
        elif estado == 6 and simbolo == "/":
            estado = 7
            token += simbolo
        elif estado == 7:
            if simbolo == "/":
                estado = 8
                token += simbolo
            else:
                estado = 7
                token += simbolo
        elif estado == 8:
            if simbolo == "/":
                token += simbolo
                return token
            else:
                estado = 7
                token += simbolo
        else:
            return


# if __name__ == "__main__":
#     comentarios_validos = ["@@comentario \n", "//com54* ss//",
#                            "//as/ddsa//", "##comentario##", "##com #as; d##"]
#     comentarios_invalidos = ["##comentario\n", "##comasd",
#                              "@@comentari", "//com54* ss/", "//as/ddsa/"]

#     for palavra in comentarios_invalidos:
#         print(comentarios(palavra))

# Reconhecer conforme exemplo:
# 2, 345, 23.5, 5.55, -4.5


def numeros(palavra):
    estado = 0
    token = ''
    aux = ''
    for simbolo in palavra:
        if estado == 0 and simbolo in DIGITOS:
            estado = 1
            token += simbolo
        elif estado == 0 and simbolo == "-":
            estado = 2
            aux += simbolo
        elif estado == 1 and simbolo in DIGITOS:
            estado = 1
            token += simbolo
        elif estado == 1 and simbolo == ".":
            estado = 3
            aux += simbolo
        elif estado == 2 and simbolo in DIGITOS:
            estado = 1
            token += aux
            aux = ''
            token += simbolo
        elif estado == 3 and simbolo in DIGITOS:
            estado = 4
            token += aux
            aux = ''
            token += simbolo
        elif estado == 4 and simbolo in DIGITOS:
            estado = 4
            token += simbolo
        else:
            return token

    return token


# if __name__ == "__main__":
#     numeros_validos = ["2", "345", "23.5", "5.55", "-4.5"]
#     numeros_invalidos = ["2.", "2.3.4", "3-5", "-3.4-"]

#     for palavra in numeros_invalidos:
#         print(numeros(palavra))
