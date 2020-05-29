from player import player

print("Hello! welcome to Chopsticks!")
players = [player(input("What is player 1 name?  ").strip()), player(input("What is player 2 name?  ").strip())]
current = 0;
opponent = 1;

#set up each player with 1 finger in each hand
def Restart():
    player1.restart()
    player2.restart()

#ask user to which hand  to split from and 
#subtract from chosen hand and add to other hand
def split():
    if players[current].canSplit():
        splits = possibleSplits(players[current].totalFingers())
        splits = removeUserHand(splits)
        
        if len(splits) == 1:
            print(f"{players[current].name} hand is now {str(splits[0])}")
            players[current].hand = splits[0]
            return True;
        message = f"Split hand to (0) {str(splits[0])} (1) {str(splits[1])} "

        try: 
            players[current].hand = splits[int(input(message).strip())]
        except Exception:
            return False
        
        return True;
    else: 
        input("You cannot split this hand you need to attack\nEnter to continue")
        return attack()

def removeUserHand(splits):
    li = list()
    for x in splits:
        playerhand = players[current].hand
        if x[0] not in playerhand:
            li.append(x)
            continue
        playerhand.remove(x[0])
        if x[1] not in playerhand:
            li.append(x)
    return li

def possibleSplits(totalfing):
    splits = list()
    n = set()

    for x in range(0, 5):
        if x > totalfing:
            #return split
            break
        if 0 <= totalfing - x  <= 5:
            if x in n:
                break
            splits.append([x % 5, (totalfing - x) % 5])
            n.add((totalfing - x) % 5)

    return splits

#add one to choosen hand   
def attack():
    return attack_helper(players[current].moves(True), players[opponent].moves(False))

def attack_helper(i, j):
    if i < 0 or i > 1:
        return False
    if j < 0 or j > 1:
        return False
    sumfinger = players[current].hand[i] + players[opponent].hand[j]
    players[opponent].hand[j] = 0 if sumfinger >= 5 else sumfinger
    return True  

while(True):
    
    print(f"{players[current].name} turn: (S)plit or (A)ttack")
    print(f"{str(players[current])} {str(players[opponent])}")
    choice = input("You choose: ").strip().upper()
    if choice == 'S':
        if split():
            opponent = current
            current = (current + 1) % 2
        else:
            print("Invalid inputs try again or (q)uit")
            
    elif choice == 'A':
        if attack():
            input("Enter to continue")
            if players[opponent].lost():
                print(f"{players[current].name} Won")
                exit()
            opponent = current
            current = (current + 1) % 2
        else:
            print("Invalid inputs try again or (q)uit")

    elif choice == "Q":
        exit()

    else:
        print("Invalid inputs try again or (q)uit")
    
