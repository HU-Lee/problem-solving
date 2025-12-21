class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        n = len(strs)
        l = len(strs[0])
        
        # Array that checks sorted state
        is_sorted = [False] * (n-1)
        deleted = 0

        for i in range(l):
            should_delete = False
            for j in range(n-1):
                # If not sorted and against the order, delete.
                if strs[j][i] > strs[j+1][i] and is_sorted[j] == False:
                    should_delete = True
                    break
                # Not update sorted state in this section

            if should_delete:
                deleted += 1
                continue            
            
            for j in range(n-1):
                # Update sorted state
                if strs[j][i] < strs[j+1][i]:
                    is_sorted[j] = True
                    
            if False not in is_sorted:
                break
        
        return deleted