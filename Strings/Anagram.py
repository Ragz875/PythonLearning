def anagram(str1,str2):
    print(len(str1),len(str2),)
    if len(str1) == len(str2):
        count=0
        for char in str1:
            if char in str2:
                count+=1
        if count==len(str1):
            return True
    else:
        return False

def rotate(str,d):
    Lfirst= str[0:d]
    Lsecond= str[d::]
    Rfirst=  str[0:len(str)-d]
    Rsecond= str[len(str)-d:]

    print("Left Rotation : ", (Lsecond + Lfirst))
    print("Right Rotation : ", (Rsecond + Rfirst))

str1=''
str2=''
print(anagram(str1,str2))
rotate('raghu',2)
