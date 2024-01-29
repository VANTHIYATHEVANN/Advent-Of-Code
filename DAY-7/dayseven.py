f=open('inputfile.txt')
mapping = {"T": "A", "J": "B", "Q": "C", "K": "D", "A": "E"}
sets_a = []
sets_b=[]
for line in open('inputfile.txt'):
    hand, amount = line.split()
    sets_a.append((hand, int(amount)))
    sets_b.append((hand, int(amount)))
def scoring(hand):
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
def value(hand):
    li=[]
    for card in hand:
        if card in mapping:
            li.append(mapping[card])
        else:
            li.append(card)
    return(scoring(hand),li)
sets_a.sort(key=lambda play: value(play[0]))
total = 0
inc = 1
for hand, amount in sets_a:
    total += inc * amount
    inc += 1
print("Part 1:",total)

mapp = {"T": "A", "J": ".", "Q": "C", "K": "D", "A": "E"}
def replacements(hand):
    if hand == "":
        return [""]

    return [
        x + y
        for x in ("23456789TQKA" if hand[0] == "J" else hand[0])
        for y in replacements(hand[1:])
    ]
def strength(hand):
    li=[]
    for card in hand:
        if card in mapping:
            li.append(mapp[card])
        else:
            li.append(card)
    return(max(map(scoring, replacements(hand))),li)

sets_b.sort(key=lambda play: strength(play[0]))
tot = 0
inc = 1
for hand, amount in sets_b:
    tot += inc * amount
    inc += 1
print("Part 2:",tot)
