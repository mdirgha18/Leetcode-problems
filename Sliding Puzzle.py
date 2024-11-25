class Solution:
    class BoardState:
        def __init__(self, initBoard, zeroX, zeroY, bfsLevel):
            self.board = initBoard #Current board configuration
            self.x = zeroX         # X position of the empty square (0)
            self.y = zeroY # Y position of the empty square (0)
            self.level = bfsLevel #Number of moves taken to reach this state

    def slidingPuzzle(self, board: List[List[int]]) -> int:
        x, y = 0, 0 #Initialize the positions of the empty square

        # Find the position of empty square (0) in the board
        for i in range(2):
            for j in range(3):
                if board[i][j] == 0:
                    x, y = i, j
                    break

        state = self.BoardState(board, x, y, 0) # Create the initial board state
        end = "123450" #Target configuration
        bfs = deque() #BFS queue
        bfs.append(state) #Append the initial state into the queue
        v = set() # set to track visited states
        v.add(self.boardToString(board)) #Add the initial state into the visited set

        while bfs: 
            curr = bfs.popleft() # Get the current state from the queue

            #Check if we have reached the target configuration 
            if self.boardToString(curr.board) == end:
                return curr.level #Return the number of moves taken 

                # we can also use loop to make the code shorter, here, we use "if" to each case to make it easy to understand

            #Go up 
            if curr.x != 0 :
                arr = [row[:] for row in curr.board] #Copy the current board
                arr[curr.x][curr.y], arr[curr.x-1][curr.y] = arr[curr.x-1][curr.y], arr[curr.x][curr.y] #Swap with the tile above
                if self.boardToString(arr) not in v: # Check if this state has been visited
                    next_state = self.BoardState(arr, curr.x-1, curr.y, curr.level+1) # Create the next state
                    bfs.append(next_state) #Append the next state into the queue
                    v.add(self.boardToString(arr)) #Mark this state as visited

            # Go left
            if curr.y != 0:
                arr = [row[:] for row in curr.board] #Copy the current board
                arr[curr.x][curr.y], arr[curr.x][curr.y-1] = arr[curr.x][curr.y-1], arr[curr.x][curr.y] #Swap with the tile to the left
                if self.boardToString(arr) not in v: # Check if this state has been visited
                    next_state = self.BoardState(arr, curr.x, curr.y-1, curr.level+1) # Create the next state
                    bfs.append(next_state) # Append the next state into the queue
                    v.add(self.boardToString(arr)) # Mark this state as visited

            #Go down
            if curr.x != 1:
                arr = [row[:] for row in curr.board] #Copy the current board
                arr[curr.x][curr.y], arr[curr.x+1][curr.y] = arr[curr.x+1][curr.y], arr[curr.x][curr.y] #Sap with the tile below
                if self.boardToString(arr) not in v: #Check if this state has been visited
                    next_state = self.BoardState(arr, curr.x+1, curr.y, curr.level+1) #Create the next state
                    bfs.append(next_state) # Append the next state into the queue
                    v.add(self.boardToString(arr)) # Mark this state as visited

            #Go right 
            if curr.y != 2: 
                arr = [row[:] for row in curr.board] #Copy the current board
                arr[curr.x][curr.y], arr[curr.x][curr.y+1] = arr[curr.x][curr.y+1], arr[curr.x][curr.y] # Swap with the tile to the right
                if self.boardToString(arr) not in v: # Check if this state has been visited
                    next_state = self.BoardState(arr, curr.x, curr.y+1, curr.level+1) # Create the next state
                    bfs.append(next_state) #Append the next state into the queue
                    v.add(self.boardToString(arr)) # Mark this state as visited

        return -1 # Returns -1 if the puzzle is unsolvable 

    def boardToString(self,board):
        return ''.join(str(num) for row in board for num in row) #Convert the board to a string representation for easy comparison    
