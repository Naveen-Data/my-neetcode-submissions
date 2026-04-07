class Solution:
    def isArmstrong(self, n: int) -> bool:
        sum = 0
        num_of_digit = len(str(n))
        number = n
        while(n>0):
            last_digit = n%10
            sum += last_digit**num_of_digit
            n = n//10
        if sum == number:
            return True
        else:
            return False
        