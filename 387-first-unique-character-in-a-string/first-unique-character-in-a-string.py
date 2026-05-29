class Solution:
    def firstUniqChar(self, s: str) -> int:
        new = {}
        for i in s:
            if i in new:
                new[i] += 1
            else:
                new[i] = 1
        for index in range(len(s)):
            key = s[index]
            if new[key] == 1:
                return index
        return -1