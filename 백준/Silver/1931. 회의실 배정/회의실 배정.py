def meetingArrange(maxnum, meeting):
    count = 0
    last_meet = [-1, -1]
    meeting.sort(key=lambda x: (x[1], x[0]))
    for i in meeting:
        if last_meet[1] <= i[0]:
            last_meet = i
            count += 1
    print(count)
            

maxnum = int(input())
meeting = []
for _ in range(maxnum):
    time = list(map(int, input().split()))
    meeting.append(time)
meetingArrange(maxnum, meeting)