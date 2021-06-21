#Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order
#A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters
# Input: digits = "23" # Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]

def letterCombinations(digits):
    # If the input is empty, immediately return an empty answer array
    if len(digits) == 0: return []
    dic = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl','6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}

    def backtrack(index, path):
        if len(path) == len(digits):
            combination.append(''.join(path))
            return
        # Get the letters that the current digit maps to, and loop through them
        possible_letters=dic[digits[index]]
        #print(possible_letters)
        for letter in possible_letters:
            # Add the letter to our current path
            path.append(letter)
            # Move on to the next digit
            backtrack(index + 1,path)
            # Backtrack by removing the letter before moving onto the next
            path.pop()

    # Initiate backtracking with an empty path and starting index of 0
    combination=[]
    backtrack(0,[])
    return combination

print('Main started')
print(letterCombinations('23'))

