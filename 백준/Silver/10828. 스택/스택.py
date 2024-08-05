def mystack():
    iteration = int(input())
    mystack=[]
    
    for i in range(iteration):
        val = input().split()
        if val[0]== "push":
            mystack.append(val[1])
            
        elif val[0]=="pop":
            if len(mystack)==0:
                print("-1")
            else:
                print(mystack[-1])
                mystack.pop()
                
        elif val[0]=="size":
            print(len(mystack))
            
        elif val[0]=="empty":
            if len(mystack)==0:
                print(1)
            else:
                print(0)
                
        elif val[0]=="top":
            if len(mystack)==0:
                print(-1)
            else:
                print(mystack[-1])
        else:
            print("input error.")
            
mystack()