a,b = map(int,input().split())
if a*b > 2*(a+b):
    print(a*b)
else:
    print(2*(a+b))