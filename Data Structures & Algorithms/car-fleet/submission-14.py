class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        numFleet = 1 
        pairs = []
        for i in range(len(speed)): 
            pairs.append((position[i], speed[i]))
        pairs.sort(reverse = True )
        top = (target - pairs[0][0]) / pairs[0][-1]
        for i in range(1, len(pairs)):
                currLeftTime = (target - pairs[i][0]) / pairs[i][-1]
                if currLeftTime > top: 
                    numFleet += 1 
                    top = currLeftTime 

        return numFleet