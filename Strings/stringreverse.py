# using while
def printrev1(words):
    l = len(words) - 1
    while l >= 0:
        print(words[l], end=' ')
        l = l - 1
# using for
def printrev2(words):
    print(words)
    for i in range(len(words)-1,-1,-1):
        print(i,-i,words[i],end=' ')

# string reverse without affecting the special chars
def strReverse(str):
    arrayChar=[str[i] for i in range(len(str))]
    print('converted to an Array :', arrayChar)

    j=len(arrayChar)-1
    i=0
    print(i,j,len(arrayChar)//2)
    while i <= len(arrayChar)//2:
        #print(arrayChar[i],arrayChar[i].isalnum(),arrayChar[j],arrayChar[j].isalnum())
        if arrayChar[i].isalnum() and arrayChar[j].isalnum():
            arrayChar[i],arrayChar[j]=arrayChar[j],arrayChar[i]
            #print('both match swapped',arrayChar[i], arrayChar[i].isalnum(), arrayChar[j], arrayChar[j].isalnum())
        elif arrayChar[i].isalnum()==True and  arrayChar[j].isalnum()== False:
            #print('i is alpha:', arrayChar[i], arrayChar[i].isalnum(), arrayChar[j], arrayChar[j].isalnum())
            j=j-1
            continue
        elif arrayChar[i].isalnum() == False and arrayChar[j].isalnum() == True:
            #print('j is alpha:', arrayChar[i], arrayChar[i].isalnum(), arrayChar[j], arrayChar[j].isalnum())
            i=i+1
            continue
        i=i+1
        j=j-1

    rs=''
    print('Array reverse :', rs.join(arrayChar))




s='my#first$'
#words=s.split(' ')
#printrev1(words)
#printrev2(words)
strReverse(s)

