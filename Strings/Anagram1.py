def anagram(input_str):
    sorted_str=''.join(sorted(input_str))
    if sorted_str not in dic:
        dic[sorted_str]=1
    else:
        dic[sorted_str] += 1

dic = {}
listt=['ABCD','AC','ADBC','PQ','QP','PAB','ACBD']
for string in listt:
    anagram(string)
print('dictionary :',dic)
count=0
for key,val in dic.items():
    if val > 1:
        count += val
print('Number of Anagrams in provided list :',count)


