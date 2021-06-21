# For sequence a1, a2, .. an find the length of longest increasing subsequence.
# elements can be in any order
# ai1, ai2,..aik
#LIS[3 1 8 2 5) --> 1->2->5 --> 3

def LIS(a):
    L=[1 for i in range(len(a))]

    for i in range(1,len(L)):
        Subprobelms=[ L[j] for j in range(i) if a[j] < a[i]]
        L[i] = 1 + max(Subprobelms,default=0)
    return max(L,default=0)

if __name__=='__main__':
    print('main started')
    arr=[5,2,8,6,3,6,9,5]
    arr = [3,1,8,2,5]

    print(LIS(arr))



