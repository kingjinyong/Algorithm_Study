def solution(my_string, is_prefix):
    # is_prefix = list(is_prefix)
    for i in range(len(is_prefix)):
        if len(is_prefix) > len(my_string):
            return 0
        if is_prefix[i] != my_string[i]:
            return 0
    return 1