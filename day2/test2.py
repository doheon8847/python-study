americano_price = 2000
latte_price = 3000
cappuccino_price = 4000  # 스펠링 수정

americano_count = int(input("아메리카노 판매 갯수 : ")) 
latte_count = int(input("라떼 판매 갯수 : "))
cappuccino_count = int(input("카푸치노 판매 갯수 : ")) # 스펠링 수정

# 총액 계산
total = (americano_price * americano_count) + \
        (latte_price * latte_count) + \
        (cappuccino_price * cappuccino_count)

# f-string을 사용한 깔끔한 출력
print(f"총 매출은 {total}원 입니다.")