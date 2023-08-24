class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        
        i = 0
        ret = []
        while i < len(words):
            s = len(words[i])
            ws = len(words[i])
            l = [words[i]]
            i += 1
            while i < len(words) and s + len(words[i]) + 1 <= maxWidth:
                l.append(words[i])
                s += len(words[i]) + 1
                ws += len(words[i])
                i+=1
            if i < len(words):
                k = [l[0]]
                spaces = maxWidth - ws
                req = len(l) - 1
                for j in l[1:]:
                    if spaces%req == 0:
                        space = ' ' * (spaces//req)
                    else:
                        space = ' ' * (spaces//req + 1)
                        spaces -= spaces//req + 1
                        req -= 1
                    k.append(space)
                    k.append(j)
                if len(l) == 1:
                    k.append(' ' * spaces)
                ret.append(''.join(k))
            else:
                ret.append(' '.join(l))
                ret[-1] += ' ' * (maxWidth-s)
        return ret
            
                
                