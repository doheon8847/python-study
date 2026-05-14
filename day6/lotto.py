# lotto.py
import random
def get_lotto():
    numbers=[] #비어있는리스트
    while len(numbers) < 6:
        n=random.randint(1,45)


        if n not in numbers:
            numbers.append(n)
                    

