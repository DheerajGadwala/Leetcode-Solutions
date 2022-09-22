class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.split(" ")
        s = [list(i) for i in s]
        for word in s:
            i, j = 0, len(word) - 1
            while i < j:
                word[i], word[j] = word[j], word[i]
                i += 1
                j -= 1
        s = [''.join(i) for i in s]
        return ' '.join(s)
            