l = [99 , 0, -7 , 0 , 16]
for i in range(len(l)):
    print(f"{l[i]:3} {id(l[i])}")

# 연속적인 공간이 아니라는것 , 파이썬에서는 엄밀히말하면 물리적메모리의 배열이 아니라는점.
# 배열이라는 것은 물리적인 연결이되어있는 자료구조인데, 파이썬에서는 배열은 물리적으로 연결되어있지 않다.
# 리스트는 배열이 아니다.