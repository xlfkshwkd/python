import sys

myFile = input("파일이름 입력해라.txt 붙혀서")

try:
    filename =open(myFile,'r')

except FileNotFoundError:
    print("응 파일 없어~")
    exit()

else:
    for i in range(3):
        line = filename.readline()
        print(i+1,end='')
        print(line)

filename.close()

#11