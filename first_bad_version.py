class Solution:
    def firstBadVersion(self, n: int) -> int:
        start = 1
        end = n
        while start <= end:
            mid = (start + (end-start))
            if isBadVersion(mid):
                end = mid - 1
            else:
                start = mid + 1
        return start
