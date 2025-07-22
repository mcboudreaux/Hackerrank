
n = int(input())
arr = list(map(int, input().split()))
max=-100


for i in range (n):
    if arr[i] > max:
        runner = max
        max = arr[i]
        
    elif arr[i]>runner and arr[i]!=max:
        runner = arr[i]

    print("runner:",runner)
    print("max:", max)
    print()

print( runner)