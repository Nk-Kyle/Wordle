from colorama import Fore, Style

# unicode for draw puzzle in command promt or terminal
left_down_angle = '\u2514'
right_down_angle = '\u2518'
right_up_angle = '\u2510'
left_up_angle = '\u250C'
dashes  = '\u2500' + '\u2500' + '\u2500'
bar = '\u2502'

def printGuess(guess, target):
    res = evalGuess(guess, target)
    #Print Top box lines
    for color in res:
        printSide(left_up_angle, color)
        printSide(dashes, color)
        printSide(right_up_angle,color)
        print(' ', end='')
    print()

    #Print middle box lines with letter
    for i in range(5):
        printSide(bar, res[i])
        print(' '+guess[i], end=' ')
        printSide(bar, res[i])
        print(' ', end='')
    print()

    #Print bottom box lines
    for color in res:
        printSide(left_down_angle, color)
        printSide(dashes, color)
        printSide(right_down_angle,color)
        print(' ', end='')
    print()

    return res

def evalGuess(guess, target):
    
    res = [Fore.WHITE for i in range(5)]
    checkedTarget = [False for i in range(5)]
    checked = [False for i in range(5)]
    #Check for right letter and position
    for i in range(5):
        if (guess[i] == target[i]):
            res[i] = Fore.GREEN
            checked[i] = True
            checkedTarget[i] = True

    #Checked for right letter but wrong position
    for i in range(5):
        if (not(checked[i])):
            for j in range(5):
                if (guess[i] == target[j] and not(checkedTarget[j])):
                    res[i] = Fore.YELLOW
                    checkedTarget[j] = True
                    break
    return res

def checkGuess(evaluations):
    for eval in evaluations:
        if (eval != Fore.GREEN):
            return False
    return True

def printSide(side, color):
    toPrint = Style.BRIGHT + color + side + Fore.RESET + Style.RESET_ALL
    print(toPrint,end='')
    return