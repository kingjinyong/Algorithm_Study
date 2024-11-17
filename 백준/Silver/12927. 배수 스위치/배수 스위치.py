light = [0]
light.extend(list(input()))
cnt = 0
for i in range(1, len(light)):
    if 'Y' not in light:
        break
    if light[i] == 'N':
        continue
    for j in range(i, len(light)):
        if j % i == 0:
            if light[j] == 'Y':
                light[j] = 'N'
            else:
                light[j] = 'Y'
    cnt += 1
print(cnt)