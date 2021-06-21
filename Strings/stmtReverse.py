# using join
def reverse(stmt):
    print('len of the given string:',len(stmt))
    strgs=stmt.split()
    new_strgs=[]
    for i in range(len(strgs)-1,-1,-1):
        new_strgs.append(strgs[i])
    new_stmt = ' '.join(new_strgs)
    print(new_stmt, len(new_stmt))

# just concatinate and rstrip
def reverse1(stmt):
    arr=stmt.split()
    print('Original:', stmt, len(stmt))
    rev_string=''
    for i in range(len(arr)-1,-1,-1):
        rev_string+= arr[i] + ' '
    print(rev_string,len(rev_string),len(rev_string.rstrip()))
    test=rev_string.rstrip()
    print(test, len(test))
reverse1('My name is Raghavender')