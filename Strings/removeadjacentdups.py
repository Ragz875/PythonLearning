def removedups(str):
    output=[str[0]]
    for i in range(1,len(str)):
        if output and str[i]==output[-1] :  # adjacent condition
            output.pop(-1)
        else:
            output.append(str[i])
    return ''.join(output)

# time limit exceeds
def removeadjkDuplicates(s,k):
    res = ''
    st = []
    for char in s:
        if st and st[-1][0] == char:
            st[-1][1]+=1
        else:
            st.append([char,1])
        if st[-1][1] == k:
            st.pop()

    for ele,count in st:
        res+=ele*count
    return res

str='pbbcggttciiippooaais'
print(f'Original string is : {str} , after dedup')
print(removeadjkDuplicates(str,2))
