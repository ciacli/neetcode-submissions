class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        d = {}
        for card in hand:
            d[card] = d.get(card, 0) + 1
        for card in sorted(d):
            while d[card] > 0:
                for el in range(card, card + groupSize):
                    if d.get(el, 0) > 0:
                        d[el] -= 1
                    else:
                        return False
            
        return True


            
