with open('input.txt') as f:
    lines = f.readlines()
    total = 0
    for l in lines[1::]:
        total += float(l.split()[4])
        print(total)