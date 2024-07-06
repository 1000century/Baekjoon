import sys
A = ["_"] * 9
def Kant_div(A,p,r):
    q = (r - p + 1) // 3
    if p<r and q//3 !=0:
        Kant_div(A, p,      p+q-1)
        Kant_div(A, r-q+1,  r)
        Kant_merge(A,p, q, r)
        print("if",A)
        return A
    else:
        A = ["=","@","="]
        print("else",A)
        return A
def Kant_merge(A,p,q,r):
    i = q
    A1 = A[p    : p+i-1]
    A3 = A[r-i+1: r]
    A2 = ["@"]*i
    A = A1 + A2 + A3
    print("merge",A)
    return A


print(Kant_div(A,0,8))

print(A)





