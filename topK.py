class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        count ={}
        for num in nums:
            count[num] = count.get(num, 0) + 1
        sorted_nums = sorted(count, key=count.get, reverse=True)
        result = sorted_nums[:k]

        return result
