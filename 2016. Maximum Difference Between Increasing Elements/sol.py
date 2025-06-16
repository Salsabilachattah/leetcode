class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        maxx = -1 
        for i in range(len(nums)-1) :
            diff = max(nums[i+1:]) - nums[i] 
            if diff > maxx :
                maxx = diff 
        if maxx == 0  :
            maxx = -1
        return maxx