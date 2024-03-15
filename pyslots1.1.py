import random
print('SPIN TO WIN!!!')
print('$$$$$$$$$$')
print('__________')
print('|| Match 3|       O')
print('|| to win!|      /')
print('||________|__   /')
print('|| $ | $ | $ | /')
print('|| $ | $ | $ |[]')
print('|| $ | $ | $ |')
print('||-----------|')
print('||___[___]___|')
print('JUST ONE SPIN AWAY FROM WINNING BIG!!!')
print('$$$$$$$$$$')
print('FREE STARTING MONIES: 500')
print('SPIN TO WIN???')
print('[YES]  [NO]')
global monies
monies = 500
bet = 0
global SPINTOWIN
SPINTOWIN = input()
if SPINTOWIN == 'no':
    print('Well too bad!')
if SPINTOWIN == 'No':
    print('Well too bad!')
print('BET AMOUNT??')
print('50 and under [1 ROW]\n51-100 [2 ROWS]\n100+ [3 ROWS]')
bet = int(input())
monies -= bet
def printmachine():
    global first
    global second
    global third
    first = random.randint(0,9)
    second = random.randint(0,9)
    third = random.randint(0, 9)
    print('__________')
    print('|| Match 3|       O')
    print('|| to win!|      /')
    print('||________|__   /')
    print('|| x | x | x | /')
    print(f'|| {first} | {second} | {third} |[]')
    print('|| x | x | x |')
    print('||-----------|')
    print('||___[___]___|')

def printmachine2():
    global first
    global second
    global third
    global fourth
    global fifth
    global sixth
    first = random.randint(0,9)
    second = random.randint(0,9)
    third = random.randint(0, 9)
    fourth = random.randint(0,9)
    fifth = random.randint(0,9)
    sixth = random.randint(0,9)
    print('__________')
    print('|| Match 3|       O')
    print('|| to win!|      /')
    print('||________|__   /')
    print('|| x | x | x | /')
    print(f'|| {first} | {second} | {third} |[]')
    print(f'|| {fourth} | {fifth} | {sixth} |')
    print('||-----------|')
    print('||___[___]___|')

def printmachine3():
        global first
        global second
        global third
        global fourth
        global fifth
        global sixth
        global seventh
        global eighth
        global ninth
        first = random.randint(0, 9)
        second = random.randint(0, 9)
        third = random.randint(0, 9)
        fourth = random.randint(0, 9)
        fifth = random.randint(0, 9)
        sixth = random.randint(0, 9)
        seventh = random.randint(0,9)
        eighth = random.randint(0,9)
        ninth = random.randint(0,9)
        print('__________')
        print('|| Match 3|       O')
        print('|| to win!|      /')
        print('||________|__   /')
        print(f'|| {seventh} | {eighth} | {ninth} | /')
        print(f'|| {first} | {second} | {third} |[]')
        print(f'|| {fourth} | {fifth} | {sixth} |')
        print('||-----------|')
        print('||___[___]___|')

while monies > 0:
    if bet <= 50:
        printmachine()
        if first == second == third:
            monies += bet*3
            print()
            print('Wowzers! You actually won!')
            print()
            print(f'Current monies: {monies}')
        else:
            print()
            print('So close! I bet you will get it next time!')
            print()
            print(f'Current monies: {monies}')
    elif bet <50 and bet >= 100:
        printmachine2()
        if first == second == third or third == fourth == fifth:
            monies += bet*3
            print()
            print('Wowzers! You actually won!')
            print()
            print(f'Current monies: {monies}')
        elif first == second == third and third == fourth == fifth:
            monies += bet * 5
            print()
            print('Wowzers! You actually won!')
            print()
            print(f'Current monies: {monies}')
        else:
            print()
            print('So close! I bet you will get it next time!')
            print()
            print(f'Current monies: {monies}')
    elif bet >= 100:
        printmachine3()
        if first == second == third or third == fourth == fifth or seventh == eighth == ninth or seventh == second == sixth or fourth == second == ninth:
            monies += bet*3
            print()
            print('Wowzers! You actually won!')
            print()
            print(f'Current monies: {monies}')
        elif (first == second == third and third == fourth == fifth) or (first == second == third and seventh == eighth == ninth) or (third == fourth == fifth and seventh == eighth == ninth):
            monies += bet * 5
            print()
            print('Wowzers! You actually won!')
            print()
            print(f'Current monies: {monies}')
        elif first == second == third == fourth == fifth == sixth == seventh == eighth == ninth:
            monies += bet * 9
            print()
            print('Wowzers! You actually won!')
            print()
            print(f'Current monies: {monies}')
        else:
            print()
            print('So close! I bet you will get it next time!')
            print()
            print(f'Current monies: {monies}')
    print('SPIN TO WIN AGAIN???')
    print('[YES]  [NO]')
    SPINTOWIN = input()
    if SPINTOWIN == 'no':
        break
    if SPINTOWIN == 'No':
        break
    print('BET AMOUNT??')
    print('50 and under [1 ROW]\n51-100 [2 ROWS]\n100+ [3 ROWS]')
    bet = int(input())
    monies -= bet
print()
print(f'TOTAL MONIES: {monies}')
print()
if monies > 0:
    print('Please collect your winnings at the nearest Blockbuster.')
else:
    print('You lost all your monies :(')

print('Reminder: You can win over 9999% of your starting monies but can only lose 100%! See you soon!')
