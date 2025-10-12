def compute_score_word(word: str) -> int:
    score = 0
    for char in word:
        value = ord(char.lower()) - ord('a') + 1
        if char.isupper():
            value *= 2

        score += value

    return score


def battle(our_team: str, opponent: str) -> str:
    our_words = our_team.split(" ")
    opponents_words = opponent.split(" ")
    count = 0

    for our_word, opponents_word in zip(our_words, opponents_words):
        our_word_score = compute_score_word(our_word)
        opponents_word_score = compute_score_word(opponents_word)
        if our_word_score > opponents_word_score:
            count += 1
        elif opponents_word_score > our_word_score:
            count -= 1

    if count > 0:
        return "We win"
    if count < 0:
        return "We lose"
    return "Draw"
