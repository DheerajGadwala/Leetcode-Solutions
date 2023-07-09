class Solution:
    def largestVariance(self, s: str) -> int:
        alphabets = 'qwertyuiopasdfghjklzxcvbnm'
        alphabets = 'qwertyuiopasdfghjklzxcvbnm'
        alphabets = 'abcdefghijklmnopqrstuvwxyz'
        ans = 0
        for i in alphabets:
            for j in alphabets:
                l = [0]
                x, y = False, False
                for k in s:
                    if i == k:
                        if l[-1] >= 0:
                            l[-1] += 1
                        else:
                            l.append(1)
                        x = True
                    elif j == k:
                        if l[-1] <= 0:
                            l[-1] -= 1
                        else:
                            l.append(-1)
                        y = True
                if x and y:
                    for n in range(len(l)):
                        ans = max(ans, abs(l[n]) - 1)
                    curr = 0
                    flag = True
                    for o in l:
                        if curr + o < 0:
                            curr = 0
                            flag = True
                        elif curr == 0:
                            curr += o
                        else:
                            curr += o
                            flag = False
                        if flag:
                            ans = max(ans, curr - 1)
                        else:
                            ans = max(ans, curr)
        return ans
                    