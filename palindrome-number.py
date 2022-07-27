class Solution:
    def isPalindrome(self, x: int) -> bool:
        x=str(x)
        pal=[]
        for i in x:
            pal.append(i)           
        palrev = pal[::-1]
        if pal == palrev:
             return True
        else:
             return False
