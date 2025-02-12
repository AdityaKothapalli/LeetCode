class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        numZeros = nums.count(0)


        while  numZeros!=0:
            nums.remove(0)
            nums.append(0)
            numZeros -=1
        return nums
                