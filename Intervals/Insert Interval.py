class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        int_start = 0
        sub_int = 0

        for interval in range(len(interval)):
            if 