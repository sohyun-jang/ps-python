def opening_file():
    try:
        with open("numbers.txt", "r") as file:
            lines = file.readlines()
            return lines
    except FileNotFoundError:
        print("존재하지 않는 파일입니다.")
        return None

success = []
error_message = []

lines = opening_file()

if lines:
    for idx, line in enumerate(lines, 1):
        try:
            parts = line.strip().split()
            if len(parts) != 3:
                raise ValueError("숫자 포맷 오류가 발생했습니다.")
            
            a = int(parts[0])
            operator = parts[1]
            b = int(parts[2])
            
            if operator == "+":
                result = a + b
            elif operator == "-":
                result = a - b
            elif operator == "*":
                result = a * b
            elif operator == "/":
                if b == 0:
                    raise ZeroDivisionError("0으로 나눌 수 없습니다.")
                result = a / b
            else:
                raise ArithmeticError("지원하지 않는 연산자입니다.")
            
            success.append("{} {} {} = {:.1f}".format(a, operator, b, result))
        
        except ValueError as z:
            error_message.append("Line {}: 숫자 포멧 오류가 발생했습니다.".format(idx, z))
        except ArithmeticError as y:
            error_message.append("Line {}: {}".format(idx, y))
        except ZeroDivisionError as z:
            error_message.append("Line {}: {}".format(idx, z))
        except Exception as exception:
            error_message.append("Line {}: 예상치 못한 오류 발생".format(idx))


    print("\n계산 결과:")
    for res in success:
        print(res)

    if error_message:
        print("\n오류가 발생한 줄:")
        for err in error_message:
            print(err)
