dic = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000, \
       'IV': 4, 'IX': 9, \
       'XL': 40, 'XC': 90, \
       'CD': 400, 'CM': 900}

s='MCMXCIV'
sum=0
#
i=0
while i < len(s):
#for i in range(len(s)): Continue stmt not working on for loop
    if s[i] == 'I':
        if ( i+1 < len(s) and s[i+1] == 'V' or s[i+1] == 'X' ):
            sum=sum+dic[s[i]+s[i+1]]
            print(sum)
            i=i+2
            continue # --> this is imp
    elif s[i] == 'X':
        if (i+1 < len(s)) and (s[i+1] == 'L' or s[i+1] == 'C'):
            sum=sum+dic[s[i]+s[i+1]]
            i=i+2
            continue
    elif s[i] == 'C':
        if (i + 1 < len(s)) and (s[i+1] == 'D' or s[i+1] == 'M'):
            sum = sum + dic[s[i] + s[i + 1]]
            i = i + 2
            continue
    print(f'sum=sum+dic[s[i]] : {sum}={sum}+dic[{s[i]}]')
    sum=sum+dic[s[i]]
    i = i + 1
    print(sum)


print(f'Roman {s} to int is {sum}:')


s