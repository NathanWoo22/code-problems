class Solution:
    def pacificAtlantic(self, heights: list[list[int]]) -> list[list[int]]:
 
        # BFS from all tiles that border pacific and atlantic ocean and build separate set of each
            # when processing out of queue, add to visisted set
            # check if surrounding cells have height that are equal to or greater, add to queue if so
            # if no more places to climb, nothing gets added to queue
 
        # intersection
            # use built in set operation
 
        # constants
        ROWS = len(heights)
        COLS = len(heights[0])
        q = []
        visited = set()
        pacific_set = set()
        atlantic_set = set()
 
        # pacific
        # build our starting queue
        for i in range(ROWS):
            q.append([i,0])
 
        for i in range(1,COLS):
            q.append([0,i])
 
       
        # run bfs
        while q:
 
            start = q.pop(0)
            pacific_set.add((start[0], start[1]))
 
            dirs = [[-1, 0], [1, 0], [0, -1], [0, 1]]
            for dr, dc in dirs:
 
                if 0 <= start[0] + dr and start[0] + dr < ROWS and 0 <= start[1] + dc and start[1] + dc < COLS and heights[start[0]+dr][start[1]+dc] >= heights[start[0]][start[1]] and (start[0]+dr, start[1]+dc) not in visited:
                    q.append([start[0]+dr, start[1]+dc])
                    visited.add((start[0], start[1]))
 
        # atlantic
        # build our starting queue
        for i in range(ROWS):
            q.append([i,COLS-1])
 
        for i in range(0,COLS-1):
            q.append([ROWS-1,i])
 
        visited = set()
       
        # run bfs
        while q:
 
            start = q.pop(0)
            atlantic_set.add((start[0], start[1]))
 
            dirs = [[-1, 0], [1, 0], [0, -1], [0, 1]]
            for dr, dc in dirs:
 
                if 0 <= start[0] + dr and start[0] + dr < ROWS and 0 <= start[1] + dc and start[1] + dc < COLS and heights[start[0]+dr][start[1]+dc] >= heights[start[0]][start[1]] and (start[0]+dr, start[1]+dc) not in visited:
                    q.append([start[0]+dr, start[1]+dc])
                    visited.add((start[0], start[1]))
 
        # get intersection
        ret = []
        for i in range(ROWS):
            for j in range(COLS):
                if (i,j) in atlantic_set and (i,j) in pacific_set:
                    ret.append([i,j])
 
        return ret
