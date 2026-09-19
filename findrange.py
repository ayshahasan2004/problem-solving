class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:

        def findLeft(nums, target):
            left = 0
            right = len(nums) - 1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return left

        def findRight(nums, target):
            left = 0
            right = len(nums) - 1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] <= target:
                    left = mid + 1
                else:
                    right = mid - 1
            return right

        left_index = findLeft(nums, target)
        right_index = findRight(nums, target)

        if left_index <= right_index:
            return [left_index, right_index]
        else:
            return [-1, -1]        