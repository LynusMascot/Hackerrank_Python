//Author: Rohit Goswami @lynus.mascot@gmail.com
   n = int(input())
    arr = list(map(int, input().split()))
    arr=list(set(arr))
    m=max(arr)
    
    if m in arr:
        arr.remove(m)
    
    maxm=max(arr)
    print(maxm)
    
    
