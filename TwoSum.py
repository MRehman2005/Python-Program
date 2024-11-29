class Solution:
    def twoSum(self,nums: list[int],target :int)->list[int]:
        n = len(nums)
        for i in range(n-1):
            for j in range(i+1,n):
                if nums[i] + nums[j] ==target:
                    return [i,j]
        return []
               
                    
solution = Solution()
print(solution.twoSum([2,7,11,15,6,3],9))
