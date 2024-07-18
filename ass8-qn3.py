def find_winner(votes):

    vote_count = {}

    for candidate in votes:
        if candidate in vote_count:
            vote_count[candidate] += 1
        else:
            vote_count[candidate] = 1

    max_votes = 0
    winner = None

    for candidate, count in vote_count.items():
        if count > max_votes:
            max_votes = count
            winner = candidate

    return winner

votes = ['a', 'b', 'a', 'c', 'a']

winner = find_winner(votes)
print(winner)