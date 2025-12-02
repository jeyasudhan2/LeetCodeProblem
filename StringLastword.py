class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        spaceCount =0
        i = len(s)-1
        while i >= 0 and s[i] == " ":
            i-=1


        while i>=0 and s[i] != " ":
            spaceCount+=1
            i-=1


        return spaceCount


solution = Solution()
print(solution.lengthOfLastWord("   fly me   to   the moon "))