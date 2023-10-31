n = int(input())
arr = list(map(int,input().split()))
print([i for i in arr if arr.count(i) == 1][0])
