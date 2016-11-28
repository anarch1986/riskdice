from random import randint

attacker = []
defender = []


def roll():
    while True:
        attacknum = input("\033[1mHow many units attack? \x1b[0;0m")
        try:
            attacknum = int(attacknum)
            if attacknum > 3 or attacknum <= 0:
                print("Invalid units.")
            else:
                break
        except:
            print("Invalid input.")

    while True:
        defendnum = input("\033[1mHow many units defend? \x1b[0;0m")
        try:
            defendnum = int(defendnum)
            if defendnum > 2 or defendnum <= 0:
                print("Invalid units.")
            else:
                break
        except:
            print("Invalid input.")

    print("")

    for x in range(attacknum):
        attacker.append(randint(1, 6))
    for x in range(defendnum):
        defender.append(randint(1, 6))

        attacker.sort(reverse=True)
        defender.sort(reverse=True)

    print("\033[1mDice:\x1b[0;0m")

    print ("  \033[1;31mAttacker: " +
           "-".join(map(str, attacker)) + "\x1b[0;0m")

    print ("  \033[1;34mDefender: " +
           "-".join(map(str, defender)) + "\x1b[0;0m")
    print("")


def result():
    attackerloss = 0
    defenderloss = 0
    if attacker[0] > defender[0]:
        defenderloss += 1
    else:
        attackerloss += 1

    if len(attacker) > 1 and len(defender) > 1:
        if attacker[1] > defender[1]:
            defenderloss += 1
        else:
            attackerloss += 1

    print("\033[1mOutcome:\x1b[0;0m")

    print ("  \033[1;31mAttacker: Lost " +
           str(attackerloss) + " unit \x1b[0;0m")
    print ("  \033[1;34mDefender: Lost " +
           str(defenderloss) + " unit \x1b[0;0m")


roll()
result()
