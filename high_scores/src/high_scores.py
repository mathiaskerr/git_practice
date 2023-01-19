def latest(scores):
    return scores[-1]


def personal_best(scores):
    return max(scores)


def personal_top_three(scores):
    sort_scores(scores)
    return f"1st Place {scores[0]}, 2nd Place {scores[1]}, 3rd Place {scores[2]}"

def sort_scores(scores):
    scores.sort(reverse = True)
    return scores

def tie_scores(scores):
    sort_scores(scores)
    if len(scores) == 2:
        return f'1st place {scores[0]} and 2nd place {scores[1]}'    
    elif len(scores) == 1:
        return f'you have the only score on the board at {scores[0]}'
    elif scores[0] == scores[1] and scores[1]== scores[2]:
        return f'Top Three scores tied at {scores[0]}'
    elif scores[0] == scores[1] and scores[1]!= scores[2]:
        return f'1st and 2nd tied at {scores[0]} and 3rd place at {scores[2]}'