class Solution:
    def firstBadVersion(self, n: int) -> int:
        def binSearch(p, q):
            if p < q:
                mid = (p + q) // 2
                if isBadVersion(mid):
                    return binSearch(p, mid)
                else:
                    return binSearch(mid + 1, q)
            return p
        return binSearch(1, n)
