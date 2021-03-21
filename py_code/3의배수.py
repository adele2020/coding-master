hap, i=0,0

for i in range(1,101):
    if i % 3 == 0:
        continue #무조건 끝으로 건너뛰고 반복문으로 다시 돌아간다.
    hap += i

print("1~100의 합계(3의 배수 제외) :%d" %hap)
