import math
T = int(input())

# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    
    sumlst = 0
    casestr = input()
    caselst = casestr.split()
    intlst = list(map(int, caselst))
    sumlst = sum(intlst)
    meancase = round(sumlst/10)
    print("#"+str(test_case)+" "+str(meancase)+" ")
    