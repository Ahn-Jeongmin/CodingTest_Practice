import sys
input = sys.stdin.readline

def lightswitch(condition):
    return 0 if condition == 1 else 1

switch_num = int(input())
switch_list = list(map(int, input().split()))
student_num = int(input())

for _ in range(student_num):
    gender, number = map(int, input().split())
    if gender == 1:  
        for i in range(number - 1, switch_num, number):
            switch_list[i] = lightswitch(switch_list[i])
    else:  
        number -= 1  
        switch_list[number] = lightswitch(switch_list[number])
        for k in range(1, switch_num//2 + 1):
            if number + k >= switch_num or number - k < 0:
                break
            if switch_list[number + k] == switch_list[number - k]:
                switch_list[number + k] = lightswitch(switch_list[number + k])
                switch_list[number - k] = lightswitch(switch_list[number - k])
            else:
                break

for i in range(0, switch_num, 20):
    print(*switch_list[i:i+20])
