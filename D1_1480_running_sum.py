class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        n=len(nums)
        sum=0
        arr=[]
        for i in range(n):
            sum+=nums[i]
            arr.append(sum)
        return arr
            
            
