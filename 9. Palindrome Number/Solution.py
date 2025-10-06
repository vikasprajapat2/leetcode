class Solution:
    def isPalindrome(self, x: int) -> bool:
        orignal=x
        reversed_no = 0

        if x < 0:
            return False 
        
        while x > 0:
            lastdigit = x % 10
            reversed_no = reversed_no * 10 + lastdigit 
            x=x//10
        return orignal == reversed_no
    
sol = Solution()  
print(sol.isPalindrome(121))