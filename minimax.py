import math

def minimax(cur_depth, node_index, scores, max_turn, target_depth):
    if cur_depth == target_depth:
        return scores[node_index]
    if max_turn:
        return max(minimax(cur_depth + 1, node_index * 2, scores, False, target_depth),
                   minimax(cur_depth + 1, node_index * 2 + 1, scores, False, target_depth))
    else:
        return min(minimax(cur_depth + 1, node_index * 2, scores, True, target_depth),
                   minimax(cur_depth + 1, node_index * 2 + 1, scores, True, target_depth))

scores = [3, 5, 2, 9, 12, 5, 23, 23]
tree_depth = math.log(len(scores), 2)
print("The optimal value is:", end=" ")
print(minimax(0, 0, scores, True, tree_depth))