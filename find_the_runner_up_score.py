if __name__ == '__main__':
    n = int(input()) 
    
    arr = list(map(int, input().split()))  
    
    max_score = max(arr)  
    
    while max_score in arr:
        arr.remove(max_score)
    
    runner_up_score = max(arr)  
    print(runner_up_score)
