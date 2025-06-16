class Solution:
 def robotWithString(self,s: str) -> str:
    min_suffix = [None] * len(s)
    min_suffix[-1] = s[-1]
    for i in range(len(s) - 2, -1, -1):
        min_suffix[i] = min(s[i], min_suffix[i + 1])
    
    t = []  
    p = []  
    i = 0
    
    while i < len(s) or t:
        while t and (i == len(s) or t[-1] <= min_suffix[i]):
            p.append(t.pop())
        if i < len(s):
            t.append(s[i])
            i += 1

    return ''.join(p)
        