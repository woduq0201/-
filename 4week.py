a = input("1. 입력한 수식 계산  2. 두 수 사이의 합계: ")
if a == "1" :
    b = (input("수식을 입력하세요: "))
    ans = eval(b)
    print (b,"결과는",ans )

if a == "2" : 
    num1 = int(input("첫번째 숫자를 입력하세요 :"))
    num2 = int(input("두번째 숫자를 입력하세요 :"))
    num3 = 0
    for num in range(num1,num2+1) :
        num3 += num
    print(num1,"+...+",num2,"는",num3,"입니다")