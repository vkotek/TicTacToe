class Game(object):
    
    def __init__(self, size=4, win=3):
        # Initiate a game with two players, call the create board method
        self.over = False
        self.P1 = "x"
        self.P2 = "o"
        self.turn = 0
        self.size = size
        self.win = win
        self.board = self.board_setup()
        print("Board of size %i created. Get %i in a row to win!" % (size, win))
        print(self)

    def __str__(self):
        # return the board when object is printed
        for row in range(self.size):
            print("-"*self.size*4+"-")
            for cell in range(self.size):
                print("| %s " % self.board[row][cell], end="")
            print("|")
        print("-"*self.size*4+"-")
        return ""
    
    def board_setup(self):
        self.board = []
        for row in range(self.size):
            row = []
            for cell in range(self.size):
                row.append(" ")
            self.board.append(row)
        return self.board
    
    def player(self):
        # determine who's turn it is (what symbol is to be used)
        if self.turn % 2 == 0:
            return "x"
        else:
            return "o"
    
    def next_turn(self):
        self.turn += 1

    def place(self, xy):
        # place a XO on field
        if self.board[xy[1]][xy[0]] != " ":
            print("This spot is already taken!")
            raise valueError
        self.board[xy[1]][xy[0]] = self.player()
        self.check_win(xy)
        self.turn += 1
        
    def check_win(self, xy):
        
        directions = [[0,1], [1,0], [1,1], [1,-1]]
        
        # check pos - win_size to pos + win_size, if win score is reached, call victory.
        for direction in directions:
            streak = 0
            cell = [x*-self.win for x in direction]
            for step in range(self.win*2-1):
                cell[0] += direction[0]
                cell[1] += direction[1]
                if self.board[cell[0]][cell[1]] == self.player():
                    streak += 1
                    if streak == self.win:
                        self.victory()
                        break
                else:
                    streak = 0

    def victory(self):
        self.over = True
        print("Player %s wins!" % self.player())
    
    def play(self):
        while not self.over:
            print("%s plays:" %self.player())
            try:
                x = int(input("x:"))-1
                y = int(input("y:"))-1
                self.place([x,y])
            except:
                print("Invalid move, go again")
            print(self)
            
   
g = Game()
g.play()
