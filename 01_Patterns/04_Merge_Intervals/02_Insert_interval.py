"""
Insert Interval (medium)
We'll cover the following
Problem Statement #
Given a list of non-overlapping intervals sorted by their start time, insert a given interval at the correct position and merge all necessary intervals to produce a list that has only mutually exclusive intervals.

Example 1:

Input: Intervals=[[1,3], [5,7], [8,12]], New Interval=[4,6]
Output: [[1,3], [4,7], [8,12]]
Explanation: After insertion, since [4,6] overlaps with [5,7], we merged them into one [4,7].
Example 2:

Input: Intervals=[[1,3], [5,7], [8,12]], New Interval=[4,10]
Output: [[1,3], [4,12]]
Explanation: After insertion, since [4,10] overlaps with [5,7] & [8,12], we merged them into [4,12].
Example 3:

Input: Intervals=[[2,3],[5,7]], New Interval=[1,4]
Output: [[1,4], [5,7]]
Explanation: After insertion, since [1,4] overlaps with [2,3], we merged them into one [1,4].
"""

"""
start end use two pointers 
"""
def insert_interval(intervals, newInterval):
    intervals.sort(key=lambda x:x[0])
    start = newInterval[0]
    end = newInterval[1]
    next_pos = 0
    matched = []
    while intervals[next_pos][0] < start:
        matched.append([intervals[next_pos]])
        next_pos+=1
    for interval in intervals:
        curr_start = interval[0]
        curr_end = interval[1]

        if curr_start <= end:
            end = max(end, curr_end)

        else:
            matched.append([start, end])
            start = curr_start
            end = curr_end
    matched.append([start, end])
    print(matched)


insert_interval([[2, 3], [5, 7]], [1, 4])

insert_interval([[1, 3], [5, 7], [8, 12]], [4, 10])


        
        

        

    