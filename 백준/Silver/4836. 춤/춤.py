import sys

def check_dance(dance):
    steps = dance.split()
    num = []
    for i in range(len(steps)):
        if steps[i] == "dip":
            if not ((i > 0 and steps[i-1] == "jiggle") or (i > 1 and steps[i-2] == "jiggle") or (i < len(steps) - 1 and steps[i+1] == "twirl")):
                num.append(1)
                steps[i] = "DIP"

    if not (len(steps) >= 3 and steps[-3:] == ["clap", "stomp", "clap"]):
        num.append(2)

    if "twirl" in steps and "hop" not in steps:
        num.append(3)

    if steps[0] == "jiggle":
        num.append(4)

    if "dip" not in steps and "DIP" not in steps:
        num.append(5)

    if not num:
        print(f"form ok: {' '.join(steps)}")
    elif len(num) == 1:
        print(f"form error {num[0]}: {' '.join(steps)}")
    else:
        errors = ', '.join(map(str, num[:-1])) + f" and {num[-1]}"
        print(f"form errors {errors}: {' '.join(steps)}")

input_lines = sys.stdin.read().strip().splitlines()
for line in input_lines:
    check_dance(line)
    