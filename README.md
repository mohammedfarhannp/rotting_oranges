# Rotting Oranges
_You are given an m x n grid where each cell can have one of three values:_

_0 representing an empty cell,_
_1 representing a fresh orange, or_
_2 representing a rotten orange._
_Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten._

_Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return -1._

![Puzzle](https://github.com/mohammedfarhannp/rotting_oranges/blob/orange/imgs/Puzzle.png)

The solution for this puzzle is scripted in python 3. I have used classes to create an object that takes an array as input and iterates on it to find Rotten Oranges(2) and check the horizontal and vertical adjacent indexes for Fresh Oranges(1) thus replacing it with Rotten Oranges(2).

After the iteration if there is still Fresh Oranges(1) in the Array then output `-1` else output the number iteration it took to completely rot all the Fresh Oranges(1). 

![Solution](https://github.com/mohammedfarhannp/rotting_oranges/blob/orange/imgs/Solution_Executed.png)