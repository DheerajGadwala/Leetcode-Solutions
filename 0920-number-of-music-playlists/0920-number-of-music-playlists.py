class Solution:
    def numMusicPlaylists(self, n: int, goal: int, k: int) -> int:
        mod=10**9+7
        
        @cache
        def res(i = goal, j = n):
            if i == 0 and j == 0:
                return 1
            elif i == 0 or j == 0:
                return 0
            elif j > k:
                return (res(i-1, j-1)*(n-j+1) + res(i-1,j)*(j-k)) % mod
            else:
                return (res(i-1,j-1)*(n-j+1)) % mod

        return res()