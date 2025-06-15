class Solution:
    def maxDiff(self, num: int) -> int:
        digits = str(num)

        d_max = ''
        a = ''
        for digit in digits:
            if d_max == '' and digit != '9':
                d_max = digit
                a += '9'
            elif digit == d_max:
                a += '9'
            else:
                a += digit

        d_min = ''
        b = ''
        if digits[0] != '1':
            d_min = digits[0]
            for digit in digits:
                if digit == d_min:
                    b += '1'
                else:
                    b += digit
        else:
            for digit in digits:
                if d_min == '' and digit not in ('0', '1'):
                    d_min = digit
                    b += '0'
                elif digit == d_min:
                    b += '0'
                else:
                    b += digit

        return int(a) - int(b)
