class Solution:
    def generate(self, numRows) -> List[List[int]]:
        l = [[1]]
        for i in range(1, numRows):
            k = [1]
            for j in range(len(l[i-1])-1):
                k.append(l[i-1][j]+l[i-1][j+1])
            k.append(1)
            l.append(k)
        return l
        