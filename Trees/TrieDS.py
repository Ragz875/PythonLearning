"""
Insert - o(L) - Length of the string
Search - o(L) - Length of the string
Delete - o(L) - Length of the string
Space : O(ALPHABET_SIZE * M * N) where N is number of
        strings in trie, M is the maximum length of string, ALPHABET_SIZE is 26 if we are
        only considering upper case Latin characters.

Below is the basic Trie which does not store the characters but based on index match it can tell
if the word is present or not
"""
class TrieNode:
    def __init__(self):
        # Storing the trie node references in dic saves space compare to array
        self.childrens = {}
        self.eow=False

class TrieTree:
    def __init__(self):
        self.root=TrieNode()

    def insert(self,key):
        # calculate the index
        curr = self.root
        for char in key:
            #trie_ind=ord(key[char_ind]) - ord('a')
            if char not in curr.childrens:
                curr.childrens[char]= TrieNode()

            curr=curr.childrens[char]
        curr.eow=True

    def search(self,key):

        curr=self.root
        for char in key:
            #trie_ind = ord(key[char_ind]) - ord('a')
            if char not in curr.childrens :
                return False
            curr=curr.childrens[char]
        return curr.eow

if __name__=='__main__':
    print('main started')
    words=['one','onee','two','three','four']
    output=['Not Present','Present']
    t=TrieTree()
    for word in words:
        t.insert(word)
    print('insert is completed')

#    t.display()

    testwords=['one','onee','two','twoo','three','four','fourr']
    for testword in testwords:
        print(f'{testword} is :',output[t.search(testword)])

















