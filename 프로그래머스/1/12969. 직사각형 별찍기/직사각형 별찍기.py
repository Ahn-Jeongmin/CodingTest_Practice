def x():
    x, y = map(int, input().split())
    for _ in range(y):
        print("*"*x)
        
x()