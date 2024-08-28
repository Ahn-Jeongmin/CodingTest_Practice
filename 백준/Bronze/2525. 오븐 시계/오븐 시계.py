A, B = map(int, input().split())
C = int(input())

current_time_in_minutes = A * 60 + B

end_time_in_minutes = current_time_in_minutes + C

end_hour = (end_time_in_minutes // 60) % 24
end_minute = end_time_in_minutes % 60

print(end_hour, end_minute)
