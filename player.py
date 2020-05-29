class player:
    def __init__(self, name):
        self.name = name
        self.hand = [1,1]
    
    def __str__(self):
        return f"{self.name}: [{self.hand[0]},{self.hand[1]}]"

    def restart(self):
        self.hand = [1,1]

    def handsEqual(self):
        return self.hand[0] == self.hand[1]

    def lost(self):
        return self.hand[0] == 0 and self.hand[1] == 0

    def moves(self, attacking):
        
        strmes = "attacking" if attacking else "opponent"

        if not self.handsEqual():
            
            if self.hand[0] == 0:
                print(f"{strmes} hand is [1] {self.hand[1]}")
                return 1

            if self.hand[1] == 0:
                print(f"{strmes} hand is [0] {self.hand[0]}")
                return 0
            
            message = f"Choose {strmes} hand (0) {self.hand[0]} (1) {self.hand[1]} "
            return int(input(message).strip())
            
        print(f"{strmes} hand is [0] {self.hand[0]}")
        return 0

    def totalFingers(self):
        return self.hand[0] + self.hand[1]
    
    def canSplit(self):
        if self.handsEqual():
            return False
        if self.totalFingers() == 1:
            return False
        return True