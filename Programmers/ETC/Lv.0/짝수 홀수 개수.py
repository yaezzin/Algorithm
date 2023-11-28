def solution(num_list):
    answer = []

    num1 = [1 for s in num_list if s % 2 == 0]
    num2 = [1 for s in num_list if s % 2 != 0]
    
    answer.append(sum(num1))
    answer.append(sum(num2))
    
    return answer
