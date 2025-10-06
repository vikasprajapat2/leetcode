class Solution:
    def isPalidrome(self, x: int) -> bool:
        orignal = x
        reversed_number = 0

        if x< 0 :
            return 0
        
        while x > 0:
            last_digit = x % 10
            reversed_number = reversed_number * 10 + 1
            x = x // 10

        return orignal == reversed_number 

                