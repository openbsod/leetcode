class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        if len(nums) == len(set(nums)):
            return False
        else:
            values = {}
            for pos, val in enumerate(nums):
                if (val in values) and (pos - values[val] <= k):
                    return True
                else:
                    values[val] = pos
            return False
