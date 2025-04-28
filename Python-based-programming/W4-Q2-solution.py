#
scores = list(map(int,input("점수를 입력하세요 (예: 90 85 100 73): ").split()))

def analyze_scores(scores, round_digit=1):
    minimum = min(scores)
    maximum = max(scores)
    average = round(sum(scores)/len(scores), round_digit)
    
    return (minimum, maximum, average)

min_val, max_val, ave_val = analyze_scores(scores)

new = filter(lambda x: x >= ave_val, scores)

print("\n최솟값: {}".format(min_val))
print("최댓값: {}".format(max_val))
print("평균값 (소수점 1자리 반올림): {}".format(ave_val))
print("평균 이상 점수: {}".format(list(new)))