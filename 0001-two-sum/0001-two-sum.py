class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_to_index = {}
        
        for index, num in enumerate(nums):
            complement = target - num
            if complement in num_to_index:
                return [num_to_index[complement], index]  # Return the indices of the complement and the current number
            num_to_index[num] = index  # Store the number and its index
        #this is used to store the index for future use
        # According to the problem statement, there will always be exactly one solution,
        # so we do not handle the case where no solution is found.
