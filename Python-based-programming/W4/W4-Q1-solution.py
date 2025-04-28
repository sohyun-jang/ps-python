num = int(input("등록할 인원 수: "))

phonebook = {}

for i in range(num):
    name, phone = input("이름과 전화번호를 입력하세요 (예: 홍길동 010-0000-1111): ").split()
    
    # 이름과 전화번호 입력 할때마다 바로 딕셔너리에 추가
    phonebook[name] = phone

while True:
    find = input("\n조회할 이름을 입력하세요 (그만두려면 stop): ")
    
    # stop으로 입력했을 때, 바로 멈춰야 하기 때문에 다른 코드들보다 앞에 적기
    if find == "stop":
        break
    
    if find in phonebook: 
        print("{}의 전화번호는 {}입니다".format(find, phonebook[find]))
    else:
        print("해당 이름 없음")
        continue


print("\n최종 전화번호 목록:")

# enumerate(phonebook.items())를 하면 (index, (key, value)) 형태로 반환되기 때문에 key와 value를 괄호로 묶으며 한 덩이로 나타내줘야함
for i, (key, value) in enumerate(phonebook.items(), start=1):
    print("{}) {}: {}".format(i, key, value))

