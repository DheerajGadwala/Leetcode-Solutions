class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        et = [0]
        n = len(intervals)
        intervals.sort(key = lambda x: x[0])
        for s, e in intervals:
            if et[0] > s:
                heappush(et, e)
            else:
                heappop(et)
                heappush(et, e)
        return len(et)