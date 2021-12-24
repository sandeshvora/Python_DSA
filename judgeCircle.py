#Robot to origin if final position same as original then return true else false

def JudgeCircle(st):
    x = 0
    y = 0
    for a in st:
        if (a == 'U'):
            y += 1
        elif (a == 'D'):
            y -= 1
        elif (a == 'L'):
            x -= 1
        elif (a == 'R'):
            x += 1

    return x==0 and y==0


print(JudgeCircle("UURR"))
