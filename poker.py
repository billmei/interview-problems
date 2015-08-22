import random

def main():
    print correctness_test()

def poker(hands):
    """Return a list of the winning hands: poker([hand,...]) => [hand,...]"""
    return allmax(hands, key=hand_rank)

def allmax(iterable, key=None):
    """Return a list of all items equal to the max of the iterable"""
    result, maxval = [], None
    key = key or (lambda x: x)
    for x in iterable:
        xval = key(x)
        if not result or xval > maxval:
            result, maxval = [x], xval
        elif xval == maxval:
            result.append(x)

    return result

def deal(num_hands, n=5, deck=[r+s for r in '23456789TJQKA' for s in 'SHDC']):
    """Return a list of num_hands different poker hands, each with n cards"""
    random.shuffle(deck)
    # Doesn't work when you want more than 52 cards total
    return [deck[n*i:n*(i+1)] for i in range(num_hands)]

def hand_rank(hand):
    """Return a value indicating the rank of a hand."""
    ranks = card_ranks(hand)
    if straight(ranks) and flush(hand):
        return (8, max(ranks))
    elif kind(4, ranks):
        return (7, kind(4, ranks), kind(1,ranks))
    elif kind(3, ranks) and kind(2, ranks):
        return (6, kind(3, ranks), kind(2, ranks))
    elif flush(hand):
        return (5, ranks)
    elif straight(ranks):
        return (4, max(ranks))
    elif kind(3, ranks):
        return (3, kind(3, ranks), ranks)
    elif two_pair(ranks):
        return (2, two_pair(ranks), ranks)
    elif kind(2, ranks):
        return (1, kind(2, ranks), ranks)
    else:
        return (0, ranks)

def card_ranks(hand):
    """Return a list of the ranks, sorted with higher first"""
    ranks = ['--23456789TJQKA'.index(r) for r,suit in hand]
    ranks.sort(reverse=True)
    return [5,4,3,2,1] if (ranks == [14,5,4,3,2]) else ranks

def straight(ranks):
    """Return True if there is a straight"""
    return (max(ranks) - min(ranks) == 4) and len(set(ranks)) == 5

def flush(hand):
    """Return True if there is a flush"""
    suits = [s for r,s in hand]
    return len(set(suits)) == 1

def kind(n, ranks):
    """Return the card for which there is n-of-a-kind, else return None"""
    for card in ranks:
        if ranks.count(card) == n: return card
    return None

def two_pair(ranks):
    """Return a tuple of two pairs if there is one, else return None"""
    hi_pair = kind(2, ranks)
    lo_pair = kind(2, list(reversed(ranks)))
    if hi_pair and (lo_pair != hi_pair):
        return (hi_pair, lo_pair)
    return None

def correctness_test():
    """Test cases for our poker program"""
    sf = "6C 7C 8C 9C TC".split() # straight flush
    fk = "9D 9H 9S 9C 7D".split() # four of a kind
    fh = "TD TC TH 7C 7D".split() # full house
    tp = "5S 5D 9H 9C 6S".split() # two pair
    s1 = "AS 2S 3S 4S 5C".split() # straight, ace low
    s2 = "2C 3C 4C 5S 6S".split() # straight
    ah = "AS 2S 3S 4S 6C".split() # ace high
    sh = "2S 3S 4S 6C 7D".split() # 7 high
    assert card_ranks(sf) == [10,9,8,7,6]
    assert card_ranks(fk) == [9,9,9,9,7]
    assert card_ranks(fh) == [10,10,10,7,7]
    fkranks = card_ranks(fk)
    tpranks = card_ranks(tp)
    assert kind(4, fkranks) == 9
    assert kind(3, fkranks) == None
    assert kind(2, fkranks) == None
    assert kind(1, fkranks) == 7
    assert two_pair(fkranks) == None
    assert two_pair(tpranks) == (9,5)
    assert straight([9,8,7,6,5]) == True
    assert straight([9,8,8,6,5]) == False
    assert flush(sf) == True
    assert flush(fk) == False
    assert poker([sf, fk, fh]) == [sf]
    assert poker([fk, fh]) == [fk]
    assert poker([fh, fh]) == [fh, fh]
    assert poker([sf]) == [sf]
    assert poker([fh]*99 + [sf]) == [sf]
    assert poker([s1, ah, sh]) == [s1]
    assert hand_rank(sf) == (8,10)
    assert hand_rank(fk) == (7,9,7)
    assert hand_rank(fh) == (6,10,7)
    return "tests passed"

def statistical_test(n=700):
    """Sample n random hands and print a table of percentages for each type of hand"""
    pass

if __name__ == '__main__':
    main()
