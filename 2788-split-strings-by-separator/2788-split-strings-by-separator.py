class Solution:
    def splitWordsBySeparator(self, words: List[str], separator: str) -> List[str]:
        ret = []
        for word in words:
            l = word.split(separator)
            for i in l:
                if i != "":
                    ret.append(i)
        return ret