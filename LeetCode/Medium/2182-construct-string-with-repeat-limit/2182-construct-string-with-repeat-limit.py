class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        # Raw heap is hard to handle limit, so count it
        counts = collections.Counter(s)

        heap = []
        for l in counts:
            heapq.heappush(heap, (-ord(l), counts[l])) # ASCII to int

        ans = ""
        while heap:
            # 1. Use first letter
            x, count = heapq.heappop(heap)
            x = chr(-x)
            use_count = min(repeatLimit, count)
            count -= use_count
            ans += x * use_count

            # 2. If exceed limit...
            if count > 0:
                if not heap: break
                y, count2 = heapq.heappop(heap)
                ans += chr(-y)
                count2 -= 1

                if count2 > 0:
                    heapq.heappush(heap, (y , count2))
                heapq.heappush(heap, (-ord(x), count))
        
        return ans
            
            