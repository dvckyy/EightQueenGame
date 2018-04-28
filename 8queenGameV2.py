import random

# Funciones de dibujo


def printNumbersHorizontal(t):
    n = len(t)
    for i in range(n):
        print("   {}".format(i), end='')
    print("")


def printHorizontalLines(t):
    n = len(t)
    print(" ", end='')
    print(("+---")*n, end='')
    print('+')


def draw(t, c):
    n = len(t)
    printNumbersHorizontal(t)
    printHorizontalLines(t)
    for i in range(n):
        s = '{}|'.format(i)
        for j in range(n):
            s += ' {} |{}'.format(c if t[i][j] == 1 else ' ' if t[i]
                                  [j] == 2 else ' ', i if j == n-1 else "")
        print(s)
        printHorizontalLines(t)
    printNumbersHorizontal(t)

# Clase Maquina


class Maquina:
    def __init__(self):
        self.values = []
        self.count = 0
        self.max_count = 10

    def isLegal2(self, t, fil, col):
        n = len(t)
        for i in range(n):
            if t[fil][i] == 1 or t[i][col] == 1:
                return False
        return True

    def generator(self, t, fil=0, col=0):
        n = len(t)
        if fil < n:
            if col < n:
                if t[fil][col] == -1:
                    if self.isLegal2(t, fil, col):
                        temp = [fil, col]
                        self.values.append(temp)
                self.generator(t, fil, col+1)
            else:
                self.generator(t, fil+1)

# Funcion Obtener Coordenadas


def getCoorXY(t, vectors, coox=0, cooy=0):
    if len(vectors) == 0:
        return "Imposible", "Imposible"
    randomNumber = random.randint(0, len(vectors)-1)
    n = len(t)
    vector = vectors[randomNumber]
    coox = vector[0]
    cooy = vector[1]
    return coox, cooy

# Funciones Basicas


def ask_play(t):
    a, b = input("Ingrese su jugada ( en terminos fil,col ): ").split(",")
    if int(a) > len(t)-1 or int(a) < 0 or int(b) > len(t)-1 or int(b) < 0:
        ask_play(t)
    return a, b


def insert_square(t, f, c):
    t[int(f)][int(c)] = 1
    t = insert_effect(t, int(f), int(c))
    return t


def insert_effect(t, f, c):
    n = len(t)
    for i in range(n):
        if t[f][i] == -1:
            t[f][i] = 2
        if t[i][c] == -1:
            t[i][c] = 2
    return t


def CrearBot():
    bot = Maquina()
    return bot


def isMoveLegal(t, col, fil):
    AuxBot = Maquina()
    return AuxBot.isLegal2(t, int(col), int(fil))


def sumScore(score):
    score += 10
    return score


n = 8
REINAS = 0
MAX_REINAS = n
MAX_ERRORES = 3
ERRORES = 0
RESULTADO = "Has Perdido"
T = [[-1, -1, -1, -1, -1],
     [-1, -1, -1, -1, -1],
     [-1, -1, -1, -1, -1],
     [-1, -1, -1, -1, -1],
     [-1, -1, -1, -1, -1]]
PLAYER_SCORE = 0
BOT_SCORE = 0
MAX_SCORE = 40

while REINAS <= MAX_REINAS or ERRORES < MAX_ERRORES:
    fil, col = ask_play(T)
    if isMoveLegal(T, fil, col):
        bot = CrearBot()
        T = insert_square(T, fil, col)
        draw(T, 'Q')
        PLAYER_SCORE += 10
        print ("Human Score = {} , Bot Score = {}".format(
            PLAYER_SCORE, BOT_SCORE))

        print("Maquina esta pensando...")
        bot.generator(T)
        AI_fil, AI_col = getCoorXY(T, bot.values)

        if AI_fil == "Imposible":
            Resultado = "Has ganado!!!"
            break

        t = insert_square(T, AI_fil, AI_col)
        draw(T, '@')

        BOT_SCORE += 10
        print ("Human Score = {} , Bot Score = {}".format(
            PLAYER_SCORE, BOT_SCORE))
        if BOT_SCORE >= MAX_SCORE:
            Resultado = "Winner Bot"
            break
        elif PLAYER_SCORE >= MAX_SCORE:
            Resultado = "Winner Human"
            break
        elif PLAYER_SCORE >= MAX_SCORE and BOT_SCORE >= MAX_SCORE:
            Resultado = "Empateee !!!!!"
            break
        REINAS += 1

    else:
        ERRORES += 1
        PLAYER_SCORE -= 5
        print ("Human Score = {} , Bot Score = {}".format(
            PLAYER_SCORE, BOT_SCORE))
        print("La jugada no es correcta , Errores = {}".format(ERRORES))

print(Resultado)
