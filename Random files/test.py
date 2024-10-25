def solution(sequence):
    if len(sequence) == 1:
        return True
        
    count = 0
    for i in range(len(sequence)-1):
        
        current = sequence[i]
        next = sequence[i+1]
        if next <= current:
            count += 1
            
        if i > 0 and i < len(sequence)-2:
            prev = sequence[i-1]
            next_2 = sequence[i+2]
            if prev >= next and current >= next_2:
                return False
                
    if count > 1:
        return False
    else:
        return True