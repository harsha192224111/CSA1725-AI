import math

def minimax_alpha_beta(cur_depth, node_index, scores, alpha, beta, max_turn, target_depth):
    if cur_depth == target_depth:
        return scores[node_index]
    
    if max_turn:
        best_value = -math.inf
        for i in range(2):
            val = minimax_alpha_beta(cur_depth + 1, node_index * 2 + i, scores, alpha, beta, False, target_depth)
            best_value = max(best_value, val)
            alpha = max(alpha, best_value)
            if beta <= alpha:
                break
        return best_value
    else:
        best_value = math.inf
        for i in range(2):
            val = minimax_alpha_beta(cur_depth + 1, node_index * 2 + i, scores, alpha, beta, True, target_depth)
            best_value = min(best_value, val)
            beta = min(beta, best_value)
            if beta <= alpha:
                break
        return best_value

scores = [3, 5, 2, 9, 12, 5, 23, 23]
tree_depth = math.log(len(scores), 2)
print("The optimal value is:", end=" ")
print(minimax_alpha_beta(0, 0, scores, -math.inf, math.inf, True, tree_depth))
