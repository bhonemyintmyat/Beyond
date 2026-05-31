class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        arsenal = numBottles #15
        while True:
            exchange = arsenal // numExchange # 15 / 4 = 3   6 / 4 = 1
            remain = arsenal % numExchange # 15%4 = 3        2
            arsenal = exchange + remain #    3+3 = 6             1+2 = 3
            numBottles += exchange # 15+3                18+1
            if arsenal < numExchange: #3 < 4
                break
        return numBottles
        