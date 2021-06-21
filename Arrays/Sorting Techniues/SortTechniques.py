# main starts here
class SortTechniques:
    def __init__(self):
        print('init is called')
    # O (n2)
    def insertionsort(self,a):
        i = 1
        print('Original Array', a)
        while i < len(a):
            j = i
            v = a[i]
            while (a[j-1] > a[j] and j >= 1):
                (a[j - 1], a[j]) = (a[j], a[j - 1])
                j = j - 1
                print('         inner loop :', a)
            a[j] = v
            i = i + 1
            print('Outer loop :', a)
# o(n2) , if it is aleady sorted a(n)
    def bubblesort(self,a):
        print('Bubble sort is called')
        print('length of an array :', a, 'is :', len(a))
        swapped = True
        for i in range(len(a)):
            if swapped:
                swapped = False
                for j in range(len(a) - 1):
                    print('i value:', i, 'j value:', j)
                    if a[j] > a[j + 1]:
                        a[j], a[j + 1] = a[j + 1], a[j]
                        swapped = True
        print('Bubble sort is completed :', a)
# o(n2)
    def selectionsort(self,a):
        print('length of an array :', a, 'is :', len(a))
        i=0
        while (i < len(a)) :
            min=i
            j=i+1
            print('    min is :', a[min])
            while (j < len(a)):
                if(a[j] < a[min]):
                    min=j
                    print('    so far min is :', a[min])
                print('    inner loop :', a)
                j=j+1
            if min != i :
                (a[i],a[min])=(a[min],a[i])
                print('outer loop :', a)
                i=i+1
            else:
                print('Already in sorted order')
                break

    def mergesort(self, arr):

        if len(arr) > 1:
            m = len(arr) // 2
            L = arr[:m]
            R = arr[m:]
            self.mergesort(L)
            self.mergesort(R)

            i=j=k=0
            while i < len(L) and j < len(R) :
                if L[i] < R[j] :
                    arr[k]=L[i]
                    i = i + 1
                else:
                    arr[k]=R[j]
                    j = j + 1
                k = k + 1

            while i < len(L):
                arr[k]=L[i]
                i = i + 1
                k = k + 1

            while j < len(R):
                arr[k] = R[j]
                j = j + 1
                k = k + 1

# Main starts here
#a=[1,2,3,4,5]
a=[-2,3,-5]
#a=[6,8,1,4,5,3,7,2]
st=SortTechniques()
#st.insertionsort(a)
#st.bubblesort(a)
#print("Orignal Array :",a)
print("sorted Array :",a)
st.mergesort(a)
#st.selectionsort(a)

print("sorted Array :",a)


