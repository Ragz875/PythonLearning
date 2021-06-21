# determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

def stringPailendrome(s):
    i=0
    pail_flag=True
    while i < len(s)//2:
        if s[i] !=s[len(s)-1-i]:
            pail_flag=False
            break
        i=i+1
    return pail_flag
s='A man, a plan, a canal: Panama'
ss=''.join(char for char in s if char.isalnum())
print(ss,stringPailendrome(ss))