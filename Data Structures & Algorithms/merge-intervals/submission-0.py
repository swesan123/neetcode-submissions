class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        # 1. Sort intervals by start
        intervals.sort(key=lambda x: x[0]) #  [[1,3],[1,5],[6,7]]
        output = []

        for interval in intervals:
            start = interval[0]  # 1, 1
            end = interval[1] # 3, 5

            # If output is empty, add first interval
            if len(output) == 0:
                output.append(interval) # [[1,3]]

            # If current interval overlaps with last interval in output
            elif start <= output[-1][1]: # 1 <= 3  
                output[-1][1] = max(output[-1][1], end) # [1, x] = max(3, 5)

            # No overlap
            else:
                output.append(interval)

        return output