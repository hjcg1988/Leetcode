class Solution:
    def countTriples(self, n: int) -> int:
        count=0
        for i in range (1,n):
             for x in range (1,n):
                if (i**2 + x**2) == n**2:
                    count += 1
                    
        return count
