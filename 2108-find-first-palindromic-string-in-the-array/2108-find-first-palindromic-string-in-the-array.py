class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        isPalindrome = lambda s: all([s[i] == s[len(s)-1-i] for i in range(len(s))])
        for word in words:
            if isPalindrome(word):
                return word
        return ""