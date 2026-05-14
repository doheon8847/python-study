#recursion.py
#재귀 호출 (함수) (함수 내부에서 자기자신을 호출)
# 5! (팩토리얼) : 1*2*3*4*5
def fact(n): 
    if n == 1:
        return 1
    else:
        return n * fact(n-1)
    

a=int(input("정수를 입력하세요")) #예) 5입력
res =fact(a) #함소 호출, 인수 a(정수) 보냄    
#반환 되어서 온 결과값을 res 저장
print(a,"!는",res,"이다") 
    
    
    #순환(재귀)함수를 활용하여 1부터 임력받은
    #숫자까지 합을 구하는 프로그램을 작성하시오
    # 입력받은 수가 5
    # 5+4+3+2+1 = 합계
    # 출력 1~5 (입력받은 숫자)까지의 합
    
def fact(n):
        if n == 1:
            return 1
        else:
            return n + fact(n - 1)
    
num = int(input("정수를 입력하시오: "))
result = fact(num)
    
print("1부터", num, "까지의 합은", result, "합니다")
    