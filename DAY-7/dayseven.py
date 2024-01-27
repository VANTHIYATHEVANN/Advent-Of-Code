f=open('inputfile.txt')
mapping = {"T": "A", "J": "B", "Q": "C", "K": "D", "A": "E"}
sets = []
for line in open('inputfile.txt'):
    hand, amount = line.split()
    sets.append((hand, int(amount)))
def classify(hand):
    counter=[]
    for c in hand:
        counter.append(hand.count(c))
    if 5 in counter:
        return 6
    if 4 in counter:
        return 5
    if 3 in counter:
        if 2 in counter:
            return 4
        return 3
    if counter.count(2) == 4:
        return 2
    if 2 in counter:
        return 1
    return 0
def strength(hand):
    return (classify(hand), [mapping.get(card, card) for card in hand])
sets.sort(key=lambda play: strength(play[0]))
total = 0
inc = 1
for hand, amount in sets:
    total += inc * amount
    inc += 1
print(total)