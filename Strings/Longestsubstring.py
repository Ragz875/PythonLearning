# longest contigious substring with non repeating characters
# Time complexity : O(n) Space complexity (Table): O(m) m is the size of the dic
def find_length_of_substring(in_str):
    max1 = 0
    max_so_far = 0
    dic = {}
    if len(in_str) == 0:
        print('longest substring non repeatable chars:', max1, 'String:',dic)
        return
    if len(in_str) == 1:
        print('longest substring non repeatable chars:', len(in_str), 'String:',in_str)
        return
    i = 0
    j = 0
    #cdffcmcpo
    while i < len(in_str):
        if in_str[i] not in dic :
            dic[in_str[i]] = i
            max_so_far += 1
            i = i + 1
        else:
            #print('Before:', dic,'max_so_far:',max_so_far,'max:',max,i,j)
            if max1 < max_so_far:
                max1=max_so_far
            max_so_far=0
            dic={}
            j=j+1
            i=j
    print('longest substring non repeatable chars:', max(max1,max_so_far), 'String:',dic)
        # print(dic)

str='cdffcmcpo'
find_length_of_substring(str)
