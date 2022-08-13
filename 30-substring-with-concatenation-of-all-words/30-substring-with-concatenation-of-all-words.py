class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        mp = dict()
        for word in words:
            mp[word] = 1 if word not in mp else mp[word] + 1
        k = len(words[0])
        t = len(words)
        ret = []
        for i in range(k):
            win = dict()
            for j in range(i, len(s), k):
                word = s[j : j + k]
                if j // k < t:
                    win[word] = 1 if word not in win else win[word] + 1
                else:
                    prev = s[j - t * k: j - t * k + k]
                    win[prev] -= 1
                    win[word] = 1 if word not in win else win[word] + 1
                    if win[prev] == 0:
                        del win[prev]
                if len(win) == len(mp):
                    flag = True
                    for w in mp:
                        flag &= mp[w] == (0 if w not in win else win[w])
                    if flag:
                        ret.append(j - t * k + k)
        return ret
                
                
        
        