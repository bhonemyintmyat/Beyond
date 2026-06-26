class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x == 0:
            return True
        if not (x < 0) and x%10 != 0:
            new = x
            rev = 0
            #x=123
            while new: 
                #rev=23
                rev = rev * 10 + (new % 10) 
                #x=12
                new //= 10
            if x == new+rev:
                return True
            else:
                return False
        else:
             return False
        