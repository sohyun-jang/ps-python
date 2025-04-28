import search_utils as su

n = [2, 4, 6, 8, 10, 12]
print("미리 정의된 리스트: {}".format(n))
target = int(input("찾을 숫자를 입력하세요: "))

# 위에 변수에 정의 해놓으면 아래 굳이 recursion function을 두번 불러오지 않아도 됌 (효율적)
result_idx = su.binary_search(n, target)

if result_idx == -1:
    result = "리스트에 존재하지 않습니다."
else:
    result = "인덱스 {}에 있습니다.".format(result_idx)

print("숫자 {}은(는) {}".format(target, result))
