


def listProd(a, b) :

    s=[]
    for i in range(len(a)):
        s.append(a[i] * b[i])
    result =sum(s)
    return print(result)

a=[1,2,3,4]
b=[4,5,6,7]

listProd(a,b)