class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        n = len(events)

        events.sort(key=lambda x: x[1])

        # end times + max values until end_times[idx]
        end_times = []
        max_values = []
        
        max_val = 0
        for start, end, value in events:
            max_val = max(max_val, value)
            end_times.append(end)
            max_values.append(max_val)
        
        answer = 0
        for start, end, value in events:
            # If 1 event
            answer = max(answer, value)

            # If 2 event
            idx = bisect_right(end_times, start - 1) - 1
            if idx >= 0:
                answer = max(answer, value + max_values[idx])
        
        return answer
