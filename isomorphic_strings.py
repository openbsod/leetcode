class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        record = {}
        if len(set(s)) != len(set(t)):
            return False
        for ss, tt in zip(s, t):
            if ss not in record:
                record[ss] = tt
            else:
                if record[ss] != tt:
                    return False
        return True
