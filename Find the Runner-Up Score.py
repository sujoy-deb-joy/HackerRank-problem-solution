n = int(input())
arr = map(int, input().split())
    
lst = sorted(set(arr), reverse=True)
print(lst[1])
    