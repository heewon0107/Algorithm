import heapq
def solution(jobs):
    jobs.sort()
    n = len(jobs)
    heap = []
        
    i, time, total_time = 0, 0, 0 
    # push job into heap
    while i < n or heap:
        
        while i < n and jobs[i][0] <= time:
            heapq.heappush(heap, (jobs[i][1], jobs[i][0]))
            i += 1
        
        if heap:
            take_time, start_time = heapq.heappop(heap)
            time += take_time
            total_time += time - start_time
        else:
            time = jobs[i][0]
        
        
    
    return total_time // n