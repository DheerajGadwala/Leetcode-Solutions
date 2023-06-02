class Solution:
    def probabilityOfHeads(self, prob: List[float], target: int) -> float:
        n = len(prob)
        @cache
        def res(pos = 0, tar = target):
            if pos == n:
                return 1 if tar == 0 else 0
            elif tar == 0:
                return (1-prob[pos]) * res(pos + 1, tar)
            else:
                return prob[pos] * res(pos + 1, tar - 1) + (1-prob[pos]) * res(pos + 1, tar)
        return res()