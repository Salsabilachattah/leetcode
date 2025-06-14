class Solution:
    def minMaxDifference(self, num: int) -> int:
        d_min = str(num)[0]
        num_min = ''
        d_max = ''
        num_max = ''
        for digit in str(num) :
            if digit == d_min :
                num_min += '0'
            else : 
                num_min += digit
            if digit != '9' and d_max == '' :
                d_max = digit
                num_max += '9'
            elif digit == d_max : 
                num_max += '9'
            else :
                num_max += digit  
        return int(num_max) - int(num_min)
        