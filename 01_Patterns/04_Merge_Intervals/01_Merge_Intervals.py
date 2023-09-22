"""
Problem Statement #
Given a list of intervals, merge all the overlapping intervals to produce a list that has only mutually exclusive intervals.

Example 1:
Intervals: [[1,4], [2,5], [7,9]]
Output: [[1,5], [7,9]]
Explanation: Since the first two intervals [1,4] and [2,5] overlap, we merged them into 
one [1,5].
"""


def merge_intervals(intervals: list[list[int]]):
    intervals.sort(key=lambda x: x[0])
    merged = []
    start, end = intervals[0][0], intervals[0][1]

    for i in range(1, len(intervals)):
        curr_interval = intervals[i]
        curr_start = curr_interval[0]
        curr_end = curr_interval[1]

        if curr_start <= end:
            end = max(end, curr_end)
        else:
            merged.append([start, end])
            start = curr_start
            end = curr_end

    merged.append([start, end])
    print(merged)


merge_intervals([[1, 4], [2, 5], [7, 9]])
