# Given a list of strings words representing an English Dictionary, find the
# longest word in words that can be built one character at a time by other words
# in words. If there is more than one possible answer, return the longest word with
# the smallest lexicographical order.

def longestword(words):
    print('testing')
    #wordset = set(words)
    words.sort()
    ans=''
    for w in words:
         if len(w) > len(ans) :
             if all(w[:i] in words for i in range(1,len(w))):
                 ans=w
    print('Result is:',ans)

# using Trie data structure

# main starts here

if __name__=='__main__':
    print('main started')
    words=['w','wo','wor','worl','world','aa']
    #words = ["a", "bbb", "banana", "app", "appl", "ap", "apply", "apple"]
    longestword(words)