class Solution:
    def countTexts(self, keys: str) -> int:
        MOD = 10**9+7
        n = len(keys)
        @cache
        def res(pos = 0):
            if pos == n:
                return 1
            a = pos + 1 < n and keys[pos] == keys[pos + 1]
            b = a and pos + 2 < n and keys[pos] == keys[pos + 2]
            c = b and (keys[pos] == '7' or keys[pos] == '9') and pos + 3 < n and keys[pos] == keys[pos + 3]
            ret = res(pos + 1) % MOD
            ret += res(pos + 2) if a else 0
            ret %= MOD
            ret += res(pos + 3) if b else 0
            ret %= MOD
            ret += res(pos + 4) if c else 0
            ret %= MOD
            return ret
        return res()