class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        insertPos = 0

        for i in range(len(nums)):
            if nums[i] != 0:
                nums[insertPos], nums[i] = nums[i], nums[insertPos]
                insertPos += 1