class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        nonzeros=[]
        zeros=[]
        for i in range(len(nums)):
            if nums[i] == 0:
                zeros.append(0)
            elif i != len(nums)-1 and nums[i]==nums[i+1]:
                    nums[i] *=2
                    nums[i+1] = 0
                    nonzeros.append(nums[i])
            else:
                nonzeros.append(nums[i])
        nums=nonzeros + zeros
        return nums
                
# Time complexity =>  O(n)          space complexity => O(n)
