import string as s

LETRAS = s.ascii_letters  # todas as letras do alfabeto
DIGITOS = s.digits  # todos os digitos de 0 a 9
SIMBOLOS_ESPECIAIS = [';', ',', '.', '+', '-', '*',
                      '(', ')', '<', '>', ':', '=', '{', '}', '/', '@', '#']


# indentificadores
# EX: exemplo de alguns identificadores válidos: i , jx , z_teste , k12aa3, u_teste123 , u_12tes3, ab#sd, a9#sd
# exemplo de alguns identificadores inválidos: z_b_bb_ , hhz_nota, 2abc, #abc, asd#, W#D#Df, 2#rt,
identificadores_validos = ['i', 'jx', 'z_teste',
                           'k12aa3', 'u_teste123', 'u_12tes3', 'ab#sd', 'a9#sd']
identificadores_invalidos = ['z_b_bb_', 'hhz_nota',
                             '2abc', '#abc', 'asd#', 'W#D#Df', '2#rt']


def identificadores(palavra):
    estado = 0

    for simbolo in palavra:
        if estado == 0 and simbolo in LETRAS:
            estado = 1
        elif estado == 1:
            if simbolo in LETRAS or simbolo in DIGITOS:
                estado = 3
            elif simbolo == "_" or simbolo == "#":
                estado = 2
            else:
                estado = None
                break
        elif estado == 2:
            if simbolo in LETRAS or simbolo in DIGITOS:
                estado = 5
            else:
                estado = None
                break
        elif estado == 3:
            if simbolo in LETRAS or simbolo in DIGITOS:
                estado = 3
            elif simbolo == "#":
                estado = 4
            else:
                estado = None
                break
        elif estado == 4:
            if simbolo in LETRAS or simbolo in DIGITOS:
                estado = 5
            else:
                estado = None
                break
        elif estado == 5:
            if simbolo in LETRAS or simbolo in DIGITOS:
                estado = 5
            else:
                estado = None
                break
        else:
            estado = None
            break

    if estado == 1 or estado == 5 or estado == 3:
        print("Identificador")
    else:
        print("cadeia não reconhecida")


# for palavra in identificadores_validos:
#     identificadores(palavra)


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

    for simbolo in palavra:
        if estado == 0:
            if simbolo in SIMBOLOS_ESPECIAIS:
                estado = 1
            elif simbolo in (":", ">"):
                estado = 2
            elif simbolo == "<":
                estado = 3
            elif simbolo == "*":
                estado = 4
            elif simbolo == "+":
                estado = 5
        elif estado == 2:
            if simbolo == "=":
                estado = 1
            else:
                estado = None
                break
        elif estado == 3:
            if simbolo in ("=", ">"):
                estado = 1
            else:
                estado = None
                break
        elif estado == 4:
            if simbolo == "*":
                estado = 1
            else:
                estado = None
                break
        elif estado == 5:
            if simbolo == "+":
                estado = 1
            else:
                estado = None
                break
        else:
            estado = None
            break

    if estado in (1, 2, 3, 4, 5):
        print("Simbolo especial")
    else:
        print("cadeia não reconhecida")


simbolos_validos = [';', ',', '.', '+', '-', '*',
                    '(', ')', '<', '>', ':', '=', '{', '}', '/', '@', '#']
simbolos_invalidos = [';;', ',,', '...', '<<',
                      '>>', '<<=', '>>=', '7', 's', '&', '%']

# for palavra in simbolos_validos:
#     simbolos_especiais(palavra)


# Reconhecer e tratar comentários:
# Para uma linha: @ @, # # Para várias linhas : inicio // fim: //

def comentarios(palavra):
    estado = 0

    for simbolo in palavra:
        if estado == 0:
            if simbolo == "#":
                estado = 3
            elif simbolo == "@":
                estado = 1
            elif simbolo == "/":
                estado = 6
            else:
                estado = None
                break
        elif estado == 1:
            if simbolo == "@":
                estado = 2
            else:
                estado = None
                break
        elif estado == 2:
            if simbolo == '\n':
                estado = 9
            else:
                estado = 2
        elif estado == 3:
            if simbolo == "#":
                estado = 4
            else:
                estado = None
                break
        elif estado == 4:
            if simbolo == "#":
                estado = 5
            else:
                estado = 4
        elif estado == 5:
            if simbolo == "#":
                estado = 9
            else:
                estado = 4
        elif estado == 6:
            if simbolo == "/":
                estado = 7
            else:
                estado = None
                break
        elif estado == 7:
            if simbolo == "/":
                estado = 8
            else :
                estado = 7
        elif estado == 8:
            if simbolo == "/":
                estado = 9
            else:
                estado = 7
        else:
            estado = None
            break

    if estado == 9:
        print("Comentário")
    else:
        print("cadeia não reconhecida")

comentarios_validos = [ "@@comentario \n", "//com54* ss//", "//as/ddsa//", "##comentario##", "##com #as; d##"]
comentarios_invalidos = ["##comentario\n","##comasd", "@@comentari", "//com54* ss/", "//as/ddsa/"]

for palavra in comentarios_invalidos:
    comentarios(palavra)

# Reconhecer conforme exemplo:
# 2, 345, 23.5, 5.55, -4.5


def numeros(palavra):
    estado = 0

    for simbolo in palavra:
        if estado == 0:
            if simbolo in DIGITOS:
                estado = 1
            elif simbolo == "-":
                estado = 2
        elif estado == 1:
            if simbolo in DIGITOS:
                estado = 1
            elif simbolo == ".":
                estado = 3
            else:
                estado = None
                break
        elif estado == 2:
            if simbolo in DIGITOS:
                estado = 1
            else:
                estado = None
                break
        elif estado == 3:
            if simbolo in DIGITOS:
                estado = 4
            else:
                estado = None
                break
        elif estado == 4:
            if simbolo in DIGITOS:
                estado = 4
            else:
                estado = None
                break
        else:
            estado = None
            break

    if estado in (1, 4):
        print("Número")
    else:
        print("cadeia não reconhecida")


numeros_validos = ["2", "345", "23.5", "5.55", "-4.5"]
numeros_invalidos = ["2.", "2.3.4", "3-5", "3.4-"]

# for palavra in numeros_validos:
#     numeros(palavra)
