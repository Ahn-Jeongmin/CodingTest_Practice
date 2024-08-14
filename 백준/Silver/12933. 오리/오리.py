import sys
input = sys.stdin.readline

audio = list(input().strip())
quack_list = []
answer = 0

for i in audio:
    if i == "q":
        if "" in quack_list:
            quack_list[quack_list.index("")] = "q"
        else:
            quack_list.append("q")
            
    elif i == "u":
        if "q" not in quack_list:
            answer = -1
            break
        else:
            quack_list[quack_list.index("q")] = "qu"
    elif i == "a":
        if "qu" not in quack_list:
            answer = -1
            break
        else:
            quack_list[quack_list.index("qu")]= "qua"
            
    elif i == "c":
        if "qua" not in quack_list:
            answer = -1
            break
        else:
            quack_list[quack_list.index("qua")]= "quac"
            
    elif i == "k":
        if "quac" not in quack_list:
            answer = -1
            break
        else:
            quack_list.remove("quac")
            quack_list.append("")
    
if answer == -1:
    print(-1)
else:
    for i in quack_list:
        if i != "":
            answer = -1
            break
    if answer != -1:
        answer = len([i for i in quack_list if i == ""])
    print(answer)