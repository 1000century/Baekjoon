import sys
A = []
T = int(sys.stdin.readline().strip())
def recursion(s, l, r):
    global cmt
    cmt = cmt + 1
    if l >= r: return 1
    elif s[l] != s[r]: return 0
    else: return recursion(s, l+1, r-1)

def isPalindrome(s):
    return recursion(s, 0, len(s)-1)


for _ in range(T):
    cmt = 0
    S = sys.stdin.readline().strip()
    print(isPalindrome(S), cmt)