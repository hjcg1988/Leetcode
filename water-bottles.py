class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        maxdrinks = numBottles 
        emptybottles = numBottles
        while emptybottles >= numExchange:
            maxdrinks += int(emptybottles/numExchange)
            emptybottles = int(emptybottles%numExchange) + int(emptybottles/numExchange)
        return maxdrinks 
