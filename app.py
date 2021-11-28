from random import randint

def getItaWord():
    with open("ita.txt") as f:
        lines = f.readlines()
        lines_len = len(lines) - 1
        ix = randint(0, lines_len)
        return lines[ix][0:-2]

def getEnWord():
    with open("en.txt") as f:
        lines = f.readlines()
        lines_len = len(lines) - 1
        ix = randint(0, lines_len)
        return lines[ix][0:-2]

def getNumber():
    return str(randint(100, 99999))

def getSpecialChar():
    pattern = '#@$%&£ç[]'
    return pattern[randint(0, len(pattern) - 1)]

psw = getItaWord() + ' ' + getEnWord() + ' ' + getItaWord() + ' ' + getEnWord() + ' ' + getNumber() + getSpecialChar()
print(psw)