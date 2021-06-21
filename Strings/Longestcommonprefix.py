# to be practised use Trie and study Trie DS
def longestCommonPrefix(strs) :
    if len(str)==0: return ''
    if len(strs) == 1:  return strs[0]

    prefix = strs[0]
    for i in range(1, len(strs)):
        word = strs[i]
        common = ""
        for j in range(min(len(prefix), len(word))):
            if prefix[j] == word[j]:
                common += word[j]
            else:
                break
        prefix = common

    return prefix

strs = ["flower","flow","flight"]
print(longestCommonPrefix(strs))
