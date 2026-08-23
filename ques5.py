n = input()
print("|i |sum|")
line = "--------"
print(line)
for i in range(1, int(n)+1):
    sum = 0
    for j in range(1, i+1):
        sum += j
    print(f"| {i}|  {sum}|")
    print(line)