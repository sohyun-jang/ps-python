# 왠만해서는 한 줄에 해결할 수 있도록, list, map, int,input, split 한 줄에 모두 해결하기
scores = list(map(int,input("점수를 입력하세요 (예: 90 85 100 73): ").split()))

def analyze_scores(scores, round_digit=1):
    minimum = min(scores)
    maximum = max(scores)
    # 소숫점 자리수 설정하는 법 : round 사용하기
    average = round(sum(scores)/len(scores), round_digit)
    
    return (minimum, maximum, average)

# 함수 외부에서 변수 설정 다시 해주기
min_val, max_val, ave_val = analyze_scores(scores)

# filter, lambda 사용하여 평균 이상 점수 리스트 새로 만들기
new = filter(lambda x: x >= ave_val, scores)

print("\n최솟값: {}".format(min_val))
print("최댓값: {}".format(max_val))
print("평균값 (소수점 1자리 반올림): {}".format(ave_val))
print("평균 이상 점수: {}".format(list(new)))