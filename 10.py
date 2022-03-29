import random



n1= random.randint(1,9)
n2= random.randint(1,9)

print("문제는 {} ".format(n1),end='')
k=int(input("* {} 이다. 정답은?".format(n2)))

sum=n1*n2
while 1:
    if k==sum:
        print("정답입니다.")
        break
    elif k==0 :
        break
    else :
        print("다시해 나가고싶으면 0")
        k = int(input(" 정답은?"))

#10
