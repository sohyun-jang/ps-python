price = input("구매한 상품 가격을 입력하세요 (공백으로 구분): ").split()
coupon = input("쿠폰 코드를 입력하세요 (없으면 NONE 입력): ")

total = 0
for i in price:
    total += int(i)
    
if 100000 <= total:
    dc = 30
elif 50000 <= total:
    dc = 20
elif 30000 <= total:
    dc = 10
    
if coupon == "VIP10":
    p_dc = 10
elif coupon == "WELCOME5":
    p_dc = 5
elif coupon == "NONE":
    p_dc = 0
    
final = total * (100-dc)/100 * (100-p_dc)/100

print("총 구매 금액: {}원".format(total))
print("기본 할인율: {}%".format(dc))
print("쿠폰 추가 할인율: {}%".format(p_dc))
print("최종 결제 금액: {}원".format(final))

# 만약 소수점 이후 숫자의 개수가 정해진 값이 있을 경우, {} 내부에 :.(소수점 이후 숫자의 개수)f를 적어 줘야 함
# 예를 들어 소수점 3자리 숫자까지 나타내야 한다면, {:.3f}로 나타낼 수 있음