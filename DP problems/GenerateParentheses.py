#Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
#Example 1: Input: n = 3
#Output: ["((()))","(()())","(())()","()(())","()()()"]

def genParentheses(n):
    output=[]

    def backtrack(s,left,right):
        if len(s) == 2 * n:
            output.append(''.join(s))
            return
        if left < n:
            s.append('(')
            backtrack(s,left+1,right)
            s.pop()

        if right < left:
            s.append(')')
            backtrack(s, left , right+1)
            s.pop()

    backtrack([],0,0)
    return output

for i in range(1,5):
    print(genParentheses(i))


