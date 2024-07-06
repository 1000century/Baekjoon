import sys
test_cases_all = sys.stdin.readlines()
test_cases = test_cases_all.rstrip().split("\n")

N = len(test_cases)
for i in range(N):     
    a,b = map(int,test_cases[i].split())
    print(a+b)
