class Solution:
    def maxDistinct(self, s: str) -> int:
        a = []
        for i in range(len(s)):
            if s[i] not in a:
                a.append(s[i])
        return len(a)
