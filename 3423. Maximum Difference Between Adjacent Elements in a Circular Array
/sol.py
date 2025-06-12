class Solution:
    def maxAdjacentDistance(self, nums: List[int]) -> int:
        maxx = 0
        for i in range(len(nums)):
            n = i+1
            if i == len(nums)-1 :
                n = 0 
            if abs(nums[i]-nums[n]) > maxx : 
                maxx = abs(nums[i]-nums[n]) 
        return maxx
        
