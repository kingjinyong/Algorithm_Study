from collections import deque

test = int(input())

for t in range(1, test + 1):
    answer = 0
    word = input()

    reverse_word_list = list(word)
    reverse_word_list.reverse()

    reverse_word = ''.join(reverse_word_list)

    # print(word, reverse_word)
    if word == reverse_word:
        answer = 1

    print(f"#{t} {answer}")
