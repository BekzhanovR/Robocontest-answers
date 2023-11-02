satr = input()
satr = "0"+satr
kesmalarSoni = 0
for i in range(0,len(satr)-1):
    if satr[i] == "0" and satr[i+1] == "1":
        kesmalarSoni += 1
print("YES" if kesmalarSoni == 1 else "NO")