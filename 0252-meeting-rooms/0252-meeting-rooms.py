class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        intervals.sort(key = lambda x: x[0])
        n = len(intervals)
        for i in range(1, n):
            if intervals[i][0] < intervals[i-1][1]:
                return False
        return True