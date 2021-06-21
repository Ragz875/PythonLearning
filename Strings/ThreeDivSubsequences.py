str='303'
temp_output=[]
# adding single digit characters
for i in range(len(str)):
    temp_output.append(str[i])
print(temp_output)
# adding combination of two pairs
for i in range(len(str)):
    for j in range(i+1,len(str)):
        temp_output.append(str[i]+str[j])
print(temp_output)


count=0

for char in temp_output:
    if (len(char) > 1 and char[0]!='0') or len(char) == 1:
        print(f'char {char}')
        if int(char)%3 == 0:
            count=count+1
print(count)
