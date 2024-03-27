import heapq

# Define the initial state and the goal state
initial_state = [5, 1, 2]
goal_state = [1, 2, 5]

# Function to calculate the Manhattan distance heuristic
def calculate_manhattan_distance(state):
    distance = 0
    for i in range(len(state)):
        if state[i] != 5:  # Change here: Checking for 5 instead of 0 for the empty tile
            # Calculate the expected row and column for the current element
            expected_row, expected_col = divmod(state[i] - 1, 3)
            # Calculate the actual row and column for the current element
            actual_row, actual_col = divmod(i, 3)
            # Add the Manhattan distance between expected and actual positions
            distance += abs(expected_row - actual_row) + abs(expected_col - actual_col)
    return distance

# Function to find the possible moves from the current state
def find_possible_moves(state):
    zero_index = state.index(5)  # Change here: Looking for index of 5 instead of 0 for the empty tile
    possible_states = []
    for move in moves:
        new_index = zero_index + move[0]*3 + move[1]
        if 0 <= new_index < len(state):
            new_state = state[:]
            new_state[zero_index], new_state[new_index] = new_state[new_index], new_state[zero_index]
            possible_states.append(new_state)
    return possible_states

# Node class for the A* search
class Node:
    def __init__(self, state, g_score, h_score, parent=None):
        self.state = state
        self.g_score = g_score
        self.h_score = h_score
        self.parent = parent

    def __lt__(self, other):
        return (self.g_score + self.h_score) < (other.g_score + other.h_score)

# A* search algorithm
def a_star_search(initial_state):
    open_set = []
    closed_set = set()
    
    heapq.heappush(open_set, Node(initial_state, 0, calculate_manhattan_distance(initial_state)))
    
    while open_set:
        current_node = heapq.heappop(open_set)

        if current_node.state == goal_state:
            path = []
            while current_node:
                path.append(current_node.state)
                current_node = current_node.parent
            return path[::-1]

        closed_set.add(tuple(current_node.state))
        
        for neighbor_state in find_possible_moves(current_node.state):
            if tuple(neighbor_state) in closed_set:
                continue
            neighbor_g_score = current_node.g_score + 1
            neighbor_h_score = calculate_manhattan_distance(neighbor_state)
            neighbor_node = Node(neighbor_state, neighbor_g_score, neighbor_h_score, current_node)
            heapq.heappush(open_set, neighbor_node)
    
    return None  # No solution found

# Define the possible moves
moves = [(0, 1), (0, -1), (1, 0), (-1, 0)]

# Example usage
solution_path = a_star_search(initial_state)
if solution_path:
    print("Solution found!")
    for i, state in enumerate(solution_path):
        print(f"Step {i + 1}:")
        for j in range(0, len(state), 3):
            print(state[j:j+3])
        print()
else:
    print("No solution found.")
