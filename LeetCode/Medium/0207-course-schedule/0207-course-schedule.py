class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Prepare topological search
        graph = [[] for _ in range(numCourses)]
        indegree = [0] * numCourses

        for pre, course in prerequisites:
            graph[course].append(pre)
            indegree[pre] += 1

        # Independent + Leaf node
        q = deque([i for i in range(numCourses) if indegree[i] == 0])

        # Iterate queue, with done lesson count
        count = 0
        while q:
            x = q.popleft()
            count += 1

            # Delete node, then, new leaf node may be created
            for node in graph[x]:
                indegree[node] -= 1
                if indegree[node] == 0:
                    q.append(node)
        
        # If not full iterated, there's cycle
        return count == numCourses