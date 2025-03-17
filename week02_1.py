import random

answer = 0
result = random.randint(1,100) # ???? 이게 뭐람
count = int(0)
win = False
while result != answer:
    answer = int(input("입력하세요 : "))
    count +=1
    if result > answer:
        print("%d는 result보다 작습니다."  %answer )
    elif result < answer:
        print(("%d는 result보다 큽니다." %answer))
    else: #result == answer:
        print("정답입니다! 답은 %d였습니다." %result)
        win = True
        break
if win :
    print("you win")
else:
    print("you over 7times, Lose")
print(count)
