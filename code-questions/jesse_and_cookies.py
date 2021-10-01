import heapq


def cookies(k, A):
    heapq.heapify(A)
    
    ops = 0
    while True:
        f = heapq.heappop(A)
                
        if f >= k:
            return ops
        
        if len(A) == 0:
            return -1
        
        s = heapq.heappop(A)
        n = f + 2*s
        heapq.heappush(A, n)
        
        ops += 1
