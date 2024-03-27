import heapq

# Define the goal state
goal_state = [[1, 2, 3],
              [4, 5, 6],
              [7, 8, 0]]

# Define the possible moves
moves = [(0, 1), (0, -1), (1, 0), (-1, 0)]

# Function to calculate the Manhattan distance heuristic
def calculate_manhattan_distance(state):
    distance = 0
    for i in range(3):
        for j in range(3):
            if state[i][j] != 0:
                #tuple containing the quotient and remainder of the division.
                x, y = divmod(state[i][j] - 1, 3) 
                #cell values start from 1, but indexing starts from 0.
                # Dividing this value by 3 gives the row index, and the remainder gives the column index
                distance += abs(x - i) + abs(y - j)
    return distance

# Function to find the possible moves from the current state
def find_possible_moves(state):
    # to store the row and column indices of the empty cell 
    zero_row, zero_col = None, None
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                zero_row, zero_col = i, j
                break
    possible_states = []
    for move in moves:
        #This line calculates the new row and column indices of the empty cell after applying the current move. 
        #It adds the corresponding values from the move tuple to the current zero_row and zero_col indices.
        new_row, new_col = zero_row + move[0], zero_col + move[1]
        #This condition checks if the new indices are within the bounds of the puzzle
        if 0 <= new_row < 3 and 0 <= new_col < 3:
            #It copies each row of the state list (which represents the current puzzle configuration) into new_state.
            #This is done to create a new puzzle configuration to avoid modifying the original one.
            new_state = [row[:] for row in state]
            #This line swaps the values of the empty cell (at indices zero_row, zero_col) and the cell at the new indices (new_row, new_col) in the new_state list
            new_state[zero_row][zero_col], new_state[new_row][new_col] = new_state[new_row][new_col], new_state[zero_row][zero_col]
            possible_states.append(new_state)
    return possible_states

# Node class for the A* search
class Node:
    def __init__(self, state, g_score, h_score, parent=None):
        self.state = state
        # cost of reaching this node from the start node
        self.g_score = g_score
        # cost from this node to the goal node 
        self.h_score = h_score
        self.parent = parent

    def __lt__(self, other):
        #allows instances of the Node class to be compared using the less than (<) operator.
        return (self.g_score + self.h_score) < (other.g_score + other.h_score)

# A* search algorithm
def a_star_search(initial_state):
    #These will be used to keep track of nodes that are yet to be explored (open_set) and nodes that have been explored (closed_set).
    open_set = []
    closed_set = set()
    print(open_set,closed_set)
    #This line pushes the initial state into the open_set as a Node object
    heapq.heappush(open_set, Node(initial_state, 0, calculate_manhattan_distance(initial_state)))
    #This line starts a loop that continues until the open_set is empty, meaning there are no more nodes to explore.
    while open_set:
        #this line pops the node with the lowest f_score from the open_set. 
        current_node = heapq.heappop(open_set)
       # Since the open_set is implemented as a min-heap, the node with the lowest f_score will be at the root, and thus it's efficiently popped off.
        # This current_node now becomes the node under evaluation.
        if current_node.state == goal_state:
            
            path = []
        #If the current node's state matches the goal state, it initiates a loop to reconstruct the path from the initial state to the goal state.
        # It iterates by tracing back through the parent pointers of each node until it reaches the initial state. 
        #At each step, it appends the state of the current node to the path.
            while current_node:
                path.append(current_node.state)
                current_node = current_node.parent
            for i in path:
                print(i)
        #Since the path was constructed by tracing back from the goal state to the initial state,
        # it needs to be reversed before returning it to ensure that it represents the correct order from the initial state to the goal state.
            return path[::-1]
        #The current node's state is added to the closed_set to mark it as explored. Since sets in Python cannot directly contain lists (as they are mutable),
        # the state is converted to a tuple of tuples to make it hashable.
        closed_set.add(tuple(map(tuple, current_node.state)))
        
        for neighbor_state in find_possible_moves(current_node.state):
            if tuple(map(tuple, neighbor_state)) in closed_set:
                continue
            neighbor_g_score = current_node.g_score + 1
            neighbor_h_score = calculate_manhattan_distance(neighbor_state)
            #A new Node object is created for the neighbor state with the computed g_score, h_score,
            # and a reference to the current node as its parent.
            neighbor_node = Node(neighbor_state, neighbor_g_score, neighbor_h_score, current_node)
            #The neighbor node is added to the open_set for further exploration.
            heapq.heappush(open_set, neighbor_node)
    
    return None  # No solution found

# Example usage
initial_state = [[1, 2, 3],
                 [0, 4, 6],
                 [7, 5, 8]]

solution_path = a_star_search(initial_state)
if solution_path:
    print("Solution found!")
    for i, state in enumerate(solution_path):
        print(f"Step {i + 1}:")
        for row in state:
            print(row)
        print()
else:
    print("No solution found.")
