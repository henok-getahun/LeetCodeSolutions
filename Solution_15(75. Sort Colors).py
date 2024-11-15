class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        if len(nums) > 1:
            leftList = nums[:len(nums)//2]
            rightList = nums[len(nums)//2:]
            self.sortColors(leftList)
            self.sortColors(rightList)

            i = 0 
            j = 0
            k = 0 

            while i < len(leftList) and j < len(rightList):
                if leftList[i] < rightList[j]:
                    nums[k] = leftList[i]
                    i += 1
                else:
                    nums[k] = rightList[j]
                    j += 1
                k += 1
            
            while i < len(leftList):
                nums[k] = leftList[i]
                i += 1
                k += 1
            while j < len(rightList):
                nums[k] = rightList[j]
                j += 1
                k += 1

              
