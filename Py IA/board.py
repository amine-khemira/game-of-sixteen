from copy import deepcopy
from os import system
from queue import Queue
from random import randint,seed


m_col=3
m_row=3
sf=5

class board:
    def __init__(self):
        self.goal= [["1","2","3"],
                    ["4","5","6"],
                    ["7","8","_"]]
        self.board=deepcopy(self.goal)
        self.empty_loc= [m_row-1,m_col-1]
        self.moves={0:self.move_up, 1:self.move_down, 2:self.move_right,3:self.move_left}

    def __repr__(self):
        for i in range(m_row):
            for j in range(m_col):
                print(self.board[i][j],"|", end="")
            print("")        
        return ""
    def refresh(self):
        system("cls")
        print(self)

        if self.goal== self.board:
            print('CONGRATS YOU DID IT !!!')
            return False
        return True

    
    def shuffle(self):
        seed()
        for i in range(100):
            m=randint(0,3)
            self.moves[m](self.board,self.empty_loc)

    def move(self,board, empty_loc, x, y):
        #verif
        if empty_loc[0]+x<0 or empty_loc[0]+x>2 or empty_loc[1]+y<0 or empty_loc[1]+y>2:
            return board,empty_loc 
        #permutation
        board[empty_loc[0]][empty_loc[1]],board[empty_loc[0]+x][empty_loc[1]+y]=board[empty_loc[0]+x][empty_loc[1]+y],board[empty_loc[0]][empty_loc[1]]
        #mise a jour
        empty_loc[0] += x
        empty_loc[1] += y
        return board, empty_loc
    def move_up(self,board,empty_loc):
        return self.move(board,empty_loc,-1,0)

    def move_right(self, board, empty_loc):
         return self.move(board,empty_loc,0,1)


    def move_down(self, board, empty_loc):
         return self.move(board,empty_loc,1,0)


    def move_left(self, board, empty_loc):
         return self.move(board,empty_loc,0,-1)
    def solve(self):
        def successors(board,loc):
            b_lst=[deepcopy(board),deepcopy(board),deepcopy(board),deepcopy(board)]
            e_loc_lst= [list(loc),list(loc),list(loc),list(loc)]

        searched = []
        fringe = Queue()

        fringe.put({"board":self.board,"e_loc":self.empty_loc,"path":[]})

        while True:
            if fringe.empty():
                return []
            
            node =fringe.get()
            if node ["board"] == self.goal:
                return node["path"]
            if node["board"] not in searched:
                searched.append(node['board'])
                for child in successors():
    
