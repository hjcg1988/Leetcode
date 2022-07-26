class Solution:
    def countTriples(self, n: int) -> int:
        squares = [i*i for i in range(1,n+1)]
        sq = set(squares)
        count=0
        for i in squares:
             for x in squares:
                if x+i > squares[-1] : break
                count += (x+i in sq)
                    
        return count
