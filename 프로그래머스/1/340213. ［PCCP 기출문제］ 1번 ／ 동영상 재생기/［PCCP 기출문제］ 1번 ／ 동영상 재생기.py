def solution(video_len, pos, op_start, op_end, commands):
    # Between text and int Transform function
    def trans(tar):
        if type(tar) == str:
            h, m = tar.split(":")
            h = int(h) * 60
            m = int(m)
            return h + m
        else:
            h = str(tar // 60)
            m = str(tar % 60)
            if len(h) == 1:
                h = "0" + h
            if len(m) == 1:
                m = "0" + m
            return h + ":" + m
    
    pos = trans(pos)
    start = trans(op_start)
    end = trans(op_end)
    video_len = trans(video_len)
    
    
        
    for c in commands:
        if start <= pos <= end:
            pos = end
        
        if c == "next":
            pos += 10
        else:
            pos -= 10
        
        if pos < 0:
            pos = 0
        elif pos > video_len:
            pos = video_len
        elif start <= pos <= end:
            pos = end
        
    return trans(pos)