def pascal(n):
    for line in range(1, n + 1):
        c = 1
        for i in range(1, line + 1):
            print(c,end='')
            c = c * (line - 1) // i
        print('')

def primeornot(n):

    if all (n%i!=0 for i in range(2,n)) and n!=1:
        return True
    return False
"""    if n%2==0 and n > 2:
        return False
    prime=True
    for i in range(2,n):
        if n%i==0:
            prime=False
            break
    return prime
"""

def find_length_of_substring(in_str):
    max1 = 0
    max_so_far = 0
    dic = {}
    if len(in_str) == 0:
        return 0
    if len(in_str) == 1:
        return 1
    i = 0
    j = 0
    while i < len(in_str):
        if in_str[i] not in dic :
            dic[in_str[i]] = i
            max_so_far += 1
            i = i + 1
        else:
            if max1 < max_so_far:
                max1=max_so_far
            max_so_far=0
            dic={}
            j=j+1
            i=j
    return max(max1,max_so_far)
a=['cdffcmcpo','defhjiilop','','a','cd' ]
for str in a:
    print(f'{str} longest substring is :', find_length_of_substring(str))