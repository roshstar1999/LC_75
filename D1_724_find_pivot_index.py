class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        n=len(nums)
        d={}
        summ=0
        #storing sum at each index eg [1,8,11,17,23,28,34]
        for i in range(n):
            summ+=nums[i]
            d[i]=summ
            
        #checking
        for i in range(n):
            #returning left edge
            if i==0 and summ-nums[i]==0:
                return 0
            
            left_sum=d[i]-nums[i]
            if left_sum==summ-left_sum-nums[i]:
                return i
        return -1
            
            
            
