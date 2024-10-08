x = input()
answer = ''
for i in x:
    if i.islower():
        answer += i.upper()
    elif i.isupper():
        answer += i.lower()
print(answer)