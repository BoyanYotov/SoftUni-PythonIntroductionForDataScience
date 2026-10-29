deck_of_cards = list(input().split())
mid = len(deck_of_cards) // 2

n = int(input())

for _ in range(n):
    first_half = deck_of_cards[:mid]
    second_half = deck_of_cards[mid:]
    shuffled_cards = []

    for _ in range(len(first_half)):
        shuffled_cards.append(first_half[_])
        shuffled_cards.append(second_half[_])

    deck_of_cards = shuffled_cards

print(deck_of_cards)
