def tester(a):
    result = []
    e= 2
    g = 2
    total = 0
    for i in a[0:8]:
        result.append(int(i) * e)
        e = e + 1

    for i in a[8:12]:
        result.append(int(i) * g)
        g = g + 1

    for i in result:
        total = total + i

    eq = 11- (total % 11)

    if str(eq) == a[12]:
        print("유효한 주민등록번호 입니다.")

    else:
        print("옳지 않은 주민등록번호 입니다.")

while True:
    a = input("주민등록번호를 입력하세요(-을 빼고 입력해주세요) : ")
    tester(a)
    print("\n -------------------- \n")
