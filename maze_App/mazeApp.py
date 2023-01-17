import numpy as np

def readMazeOneText():
    with open("maze_App/maze-one.txt", "rt") as fopened:
        contents = fopened.read()
        return contents

def representMazeOne():
    contents = readMazeOneText()
    with open("maze_App/maze-oneRepresented.txt", "wt") as fout:

        for line in contents:
            for i in line:
                if (i=='*'):
                    fout.write(line.replace('*', '0'))
                elif (i==' '):
                    fout.write(line.replace(' ', '1'))
                elif (i=='A'):
                    fout.write(line.replace('A', '2'))
                else:
                    fout.write(line.replace('B', '3'))


def find_Maze_Path():
    # opening the file
    with open('maze_App/maze-oneRepresented.txt') as file: 
    #convertng to 2D array
        array2d = [[int(digit) for digit in line.strip()] for line in file]
   
    #Creating the 2D Numpy array of maze 
    maze=np.array(array2d)

    # For maze of 17 rows and 65 columns
    for i in range(17):
        for j in range(65):
            if(maze[i][j]==2):
                maze[i][j]=1
                b=i
                a=j
  
    for i in range(17):
        for j in range(65):
            if(maze[i][j]==3):
                maze[i][j]=1
                b_dest=i # b_dest and a_dest are the coordinate of 3
                a_dest=j

    solution = [[0]*65 for _ in range(17)]
    path_of_maze = []

    def maze_solver(m, n):
        #If a_dest and b_dest are reached, maze is solved
        if (m==b_dest) and (n==a_dest):
            solution[m][n] = 1
            return True
        #checking if the cell is visitable
        if m>=0 and n>=0 and m<17 and n<65 and solution[m][n] == 0 and maze[m][n] == 1:
            #if safe to visit then visit the cell
            solution[m][n] = 1
            #Moving South
            if maze_solver(m+1, n):
                path_of_maze.insert(0, "S")
                #solution[m+1][n] = 'S'
                return True
            #Moving East
            if maze_solver(m, n+1):
                path_of_maze.insert(0, "E")
                #solution[m][n+1] = 'E'
                return True
            #Moving North
            if maze_solver(m-1, n):
                path_of_maze.insert(0, "N")
                #solution[m-1][n] = 'N'
                return True
            #Moving West
            if maze_solver(m, n-1):
                path_of_maze.insert(0, "W")
                #solution[m][n-1] = 'W'
                return True
            #cktracking
            solution[m][n] = 0
            return False
        return False

    if (maze_solver(b, a)):
        print("Path found :")
        for i in path_of_maze:
            print ( i,end="")
    else:
        print("No solution")
        
    print("\n\n Path found in the text itself represented by ones including the start and the distination: ")
    for i in solution:
        print(i)


def main():
   representMazeOne()
   find_Maze_Path()
  

if  __name__ == "__main__":
    main()


