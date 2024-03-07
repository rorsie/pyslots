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
print('SPIN TO WIN???')
print('[YES]  [NO]')
global SPINTOWIN
SPINTOWIN = input()
if SPINTOWIN == 'no':
    print('Well too bad!')
if SPINTOWIN == 'No':
    print('Well too bad!')
print('HOW MANY ROWS???')
print('[1]  [2]  [3]')
rows = int(input())
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

while True:
    if int(rows) == 1:
        printmachine()
        if first == second == third:
            print()
            print('Wowzers! You actually won! Please collect your payment at the nearest Blockbuster.')
            print()
        else:
            print()
            print('So close! I bet you will get it next time!')
            print()
    elif int(rows) == 2:
        printmachine2()
        if first == second == third or third == fourth == fifth:
            print()
            print('Wowzers! You actually won! Please collect your payment at the nearest Blockbuster.')
            print()
        else:
            print()
            print('So close! I bet you will get it next time!')
            print()
    elif int(rows) == 3:
        printmachine3()
        if first == second == third or third == fourth == fifth or seventh == second == sixth or fourth == second == ninth:
            print()
            print('Wowzers! You actually won! Please collect your payment at the nearest Blockbuster.')
            print()
        else:
            print()
            print('So close! I bet you will get it next time!')
            print()
    print('SPIN TO WIN AGAIN???')
    print('[YES]  [NO]')
    SPINTOWIN = input()
    if SPINTOWIN == 'no':
        break
    if SPINTOWIN == 'No':
        break
    print('HOW MANY ROWS???')
    print('[1]  [2]  [3]')
    rows = input()
print()
print('Reminder: You can win over 9999% of your starting money but can only lose 100%! See you soon!')
