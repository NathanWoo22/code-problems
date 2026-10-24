class Solution:
    def findRedundantConnection(self, edges: list[list[int]]) -> list[int]:
        adjList = defaultdict(list)
        for edge in edges: 
            adjList[edge[0]].append(edge[1])
            adjList[edge[1]].append(edge[0])

        visited = set()
        stack = []
        for edge in adjList.keys():
            stack.append(edge)
        
        def dfs(node, parent, dfsVisited):
            # base case
            if node in dfsVisited:
                if node < parent:
                    return [node, [[node, parent]]]
                return [node, [[parent, node]]]

            dfsVisited.add(node)
            for adj in adjList[node]:
                if adj == parent:
                    continue

                result = dfs(adj, node, dfsVisited)
                if result != None:
                    nodeToAppend = [parent, node] 
                    if parent and node < parent:
                        nodeToAppend = [node, parent]
                    
                    if result[0] == node:
                        result[0] = None

                    if result[0] != None:
                        result[1].append(nodeToAppend)
                    
                    return result
                
            return None 
        
        res = dfs(edges[0][0], None, set())
        for i in range(len(edges)):
            if edges[len(edges) - 1 - i] in res[1]:
                return edges[len(edges) - 1 - i]
        
        
