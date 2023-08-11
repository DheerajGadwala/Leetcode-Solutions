class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        coins.sort()
        @cache
        def res(curr = amount, cpos = len(coins)-1):
            if curr == 0:
                return 1
            elif curr < 0 or cpos < 0:
                return 0
            else:
                return res(curr - coins[cpos], cpos) + res(curr, cpos-1)
        return res()