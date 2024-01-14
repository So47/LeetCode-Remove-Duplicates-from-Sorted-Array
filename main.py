class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        unique_elements_count = 1

        for i in range(1, len(nums)):
            if nums[i]!= nums[unique_elements_count - 1]:
                nums[unique_elements_count] = nums[i]
                unique_elements_count +=1
    
        return unique_elements_count

        
