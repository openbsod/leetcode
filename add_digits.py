class Solution:
    def addDigits(self, num: int) -> int:
        if num <= 9:
            return num
        buf = 0
        while num > 0:
            buf += num % 10
            num //= 10
        return self.addDigits(buf)
