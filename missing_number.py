class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        length = len(nums)
        return (int((length ** 2 + length) / 2)) - sum(nums)
