
class Rotting_Oranges:
    def __init__(self, Array):
        self.Array = Array
        self.Rotten, self.Fresh, self.Empty = 2, 1, 0
        self.Minutes = 0

    def Iterate(self):
        i = 0
        while i < len(self.Array):
            j = 0
            while j < len(self.Array):
                if self.Array[i][j] == self.Rotten:
                    self.Rot(i, j)
                j += 1
            i += 1
        
        for Row in self.Array:
            for Orange in Row:
                if Orange == self.Fresh:
                    print(-1)
                    return None
        print(self.Minutes)
                    
    def Rot(self, x, y):
        Changes = False
        if len(self.Array) > x+1 >= 0 and self.Array[x+1][y] == self.Fresh:
            self.Array[x+1][y] = self.Rotten
            Changes = True
        if len(self.Array) > x-1 >= 0  and self.Array[x-1][y] == self.Fresh:
            self.Array[x-1][y] = self.Rotten
            Changes = True
        if len(self.Array) > y+1 >= 0 and self.Array[x][y+1] == self.Fresh:
            self.Array[x][y+1] = self.Rotten
            Changes = True
        if len(self.Array) > y-1 >= 0 and self.Array[x][y-1] == self.Fresh:
            self.Array[x][y-1] = self.Rotten
            Changes = True
        if Changes:
            self.Minutes += 1
        

Input = eval(input("Input: "))

Minutes = Rotting_Oranges(Input)
Minutes.Iterate()