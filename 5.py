
n=input("섭씨 입력핧래? YES 화씨 입력할래? NO")
if n=="YES" :
    TC=float(input("섭씨 온도 내놔 "))
    Tf=(9/5)*TC+32
    print("화씨는 ={}".format(Tf))
else :
    TF = float(input("화씨 온도 내놔 "))
    TC = (5 / 9) * (TF - 32)
    print("화씨는 ={}".format(TC))
