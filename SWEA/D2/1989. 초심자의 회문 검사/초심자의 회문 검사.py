test = int(input())

for t in range(1, test + 1):
    word = input()

    answer = 0
    if word == word[::-1]:
        answer = 1
        
    print(f"#{t} {answer}")
