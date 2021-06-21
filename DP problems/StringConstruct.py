# write a program that returns a boolean value which indicates whether or not the target can be
# contructed by concatiating elements of wordbank array
# m - target length, n - wordbank length
#BruteForce = O(n^m * m), space O(m*m) - Expoential in time/space
# DP memorizarton O(n*m2)
def canConstruct(targetString,wordBank,cache={}):
    if targetString == '':  return True
    if targetString in cache:   return  cache[targetString]

    # iterating through every element
    for word in wordBank:
        if targetString.startswith(word):
            suffix = targetString[len(word):]
            if canConstruct(suffix,wordBank,cache):
                cache[targetString]=True
                return True
    cache[targetString] = False
    return False

# function to retrun the number of ways targetstring is constructed from given wordbank
# O(n*m*m) from exponential to polynomial
#o(m*m)
def countConstruct(targetString, wordbank,cache={}):
    if targetString == '':  return 1
    if targetString in cache:   return cache[targetString]

    tot_ways=0
    for word in wordbank:
        if targetString.startswith(word):
            suffix=targetString[len(word):]
            ways=countConstruct(suffix,wordbank)
            tot_ways+=ways

    cache[targetString] = tot_ways
    return tot_ways

# function to return 2D array containing all the ways that the targetstring can be constructed.
# O(n^*m) still exponential because you need to return arrays of array (2D), O(m) - space

def allConstruct(targetString, wordbank,cache={}):
    if targetString=='': return [[]]
    if targetString in cache: return cache[targetString]

    result = []

    for word in wordbank:
        if targetString.startswith(word):
            suffix=targetString[len(word):]
            suffix_ways = allConstruct(suffix,wordbank,cache)
            #print('suffix_ways:', suffix_ways)
            target_ways= [ [word] + arr for arr in suffix_ways ]
            result.extend(target_ways)
    cache[targetString]=result
    return result





if __name__== '__main__':
    print('main started')
    print('abcdef :',allConstruct('abcdef',['ab','abc','cd','def','abcd']))
    print('purple :', allConstruct('purple', ['purp', 'p', 'ur', 'le', 'purpl']))
    print('eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef :',allConstruct('eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef', ['ee', 'eee', 'e', 'eeee', 'eeeee']))




