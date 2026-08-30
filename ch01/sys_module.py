import sys

print("실행 파일명 :", sys.argv[0])
for i, arg in enumerate(sys.argv[1:], start=1) :
    print('인자', i, ':', arg)
sys.exit()
for i in range(1, 100) :
    print('exit()함수로 인해 실행되지 않는다.')