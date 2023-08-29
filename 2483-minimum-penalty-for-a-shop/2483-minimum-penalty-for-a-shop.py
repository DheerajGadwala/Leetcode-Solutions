class Solution:
    def bestClosingTime(self, customers: str) -> int:
        y, n = 0, 0
        for i in customers:
            if i == 'Y':
                y+=1
            else:
                n+=1
        ans = 0
        mn = y
        y_so_far, n_so_far = 0, 0
        for i in range(len(customers)):
            if customers[i] == 'Y':
                y_so_far += 1
            else:
                n_so_far += 1
            penalty = n_so_far + y - y_so_far
            if penalty < mn:
                mn = penalty
                ans = i + 1
        return ans