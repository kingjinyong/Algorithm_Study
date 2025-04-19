def solution(numbers, target):
    values = [0]
    
    for number in numbers:
        temp = []
        
        for value in values:
            temp.append(value-number)
            temp.append(value+number)
        
        values = temp
    # print(values)
    
    return values.count(target)