import heapq

def minute(text):
    # 00:00
    h = int(text[:2])
    m = int(text[3:])
    return h * 60 + m

def solution(book_time):
        
    N = len(book_time)
    for i in range(N):
        book = book_time[i]
        book_time[i] = (minute(book[0]), minute(book[1]) + 10)
    
    book_time.sort()
    
    rooms = []
    
    for s, e in book_time:
        if rooms and rooms[0] <= s:
            heapq.heappop(rooms)
        heapq.heappush(rooms, e)

    return len(rooms)