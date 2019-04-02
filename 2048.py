# At the moment, this code contain games logic only. This basically just an 
# excersie for me in building an algortihm and practicing OOP. I'll create GUI 
# version for further development

# For playing the games you could create an object which inherited games() class
# e.g 
# play = games()
# play.up()

import numpy as np

# This games() class contain games logic. It produce an array, called arr, that
# can be access by calling games.arr. Some method could be called for altering 
# the value of games.arr. The games movements (up, down, left, right) are 
# basically the same so it could be done in two functions (lining_up and merge)  
# but with additional flips and transpose to the array.

class games():

    # This function defining number of tiles, set score to zero, create zero arr
    def __init__ (self):
        self.tiles = [4, 4]
        self.score = 0
        self.arr = np.array([[0] * self.tiles[0]] * self.tiles[1])
        self.prev = self.arr
        self.generateRandom()
        self.status = 'not over'
        print(self.arr)
        
    # This function set status to over if there is no zero element in arr     
    def check_status(self):
        if np.all(self.arr == 0) == False:
            self.status = 'over'
            
    # This function reset the games
    def reset(self):
        self.__init__()
        
    # This function generates two or for into random zero element of arr    
    def generateRandom(self):
        zero_id = np.argwhere(self.arr == 0)
        if zero_id.size != 0:
            id = zero_id[np.random.randint(len(zero_id))]
            self.arr[id[0]][id[1]] = np.random.choice([2, 4])
            
    # This function merge two element with same number
    def merge(self):
        n_row, n_col = self.arr.shape 
        for col in range(n_col):
            for row in range(n_row - 1):
                if self.arr[row + 1][col] == self.arr[row][col] and\
                self.arr[row][col] != 0:
                    self.arr[row][col] = self.arr[row][col] * 2
                    self.arr[row + 1][col] = 0
                    self.score = self.score + self.arr[row][col]
    
    # This function lining up non zero elements of arr to the top      
    def lining_up(self):
        n_row, n_col = self.arr.shape 
        new = np.array([[0] * n_col] * n_row)
        for col in range(n_col):
            idx = 0
            for row in range(n_row):
                if self.arr[row][col] != 0:
                    new[idx][col] = self.arr[row][col]
                    idx = idx + 1
        self.arr = new
        
    def up(self):
        self.lining_up()
        self.merge()
        self.lining_up()
        if np.all(self.arr == self.prev) == False:
            self.generateRandom()
            self.prev = self.arr
        print(self.arr)
        
    def down(self):
        self.arr = np.flip(self.arr, 0)
        self.lining_up()
        self.merge()
        self.lining_up()
        self.arr = np.flip(self.arr, 0)
        if np.all(self.arr == self.prev) == False:
            self.generateRandom()
            self.prev = self.arr
        print(self.arr)
    
    def left(self):
        self.arr = np.transpose(self.arr)
        self.lining_up()
        self.merge()
        self.lining_up()
        self.arr = np.transpose(self.arr)
        if np.all(self.arr == self.prev) == False:
            self.generateRandom()
            self.prev = self.arr
        print(self.arr)
        
    def right(self):
        self.arr = np.transpose(self.arr)
        self.arr = np.flip(self.arr, 0)
        self.lining_up()
        self.merge()
        self.lining_up()
        self.arr = np.flip(self.arr, 0)
        self.arr = np.transpose(self.arr)
        if np.all(self.arr == self.prev) == False:
            self.generateRandom()
            self.prev = self.arr
        print(self.arr)

                
