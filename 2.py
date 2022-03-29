n=int(input("정수 n 입려해 거기까지 더한다(짝수만 ) "))
x=1
sum = 0
while x < n:
    if x%2==0:
        sum=sum+x
    else :
        pass
    x=x+1

print(sum)

