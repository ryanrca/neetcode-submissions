"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:

        # unsure if 0 intervals == no conflicts? or false?
        if not intervals:
            return True

        used = set()

        for meeting in intervals:
            for i in range(meeting.start,meeting.end):
                if i in used:
                    return False
                used.add(i)
        return True
