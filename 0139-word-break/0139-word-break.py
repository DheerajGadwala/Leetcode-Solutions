class Solution:
    dp = dict()
    gb_var = False
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        Solution.dp=dict()
        Solution.gb_var = False
        return self.allSentences(s, wordDict)
        
    def allSentences(self, strn, words, pos=0):
        if(Solution.gb_var):
            return True
        if(pos in Solution.dp):
            return Solution.dp[pos]
        if(pos == len(strn)):
            Solution.dp[pos] = True
            Solution.gb_var = True
            return Solution.dp[pos]
        answers = []
        for i in range(len(strn), pos, -1):
            if(strn[pos:i] in words):
                #print(strn[pos:i])
                if(self.allSentences(strn, words, pos = i)):
                    Solution.dp[pos] = True
                    return True
        Solution.dp[pos] = False
        return Solution.dp[pos]