# this is different DP problem
def longestCommonSubsequence(text1, text2) :
    m, n = len(text1), len(text2)
    # build (M+1) X (N+1)
    dp = [[0] * (n+1) for _ in range(m+1)]
    print(dp)

    for i in range(1, m+1):
        for j in range(1, n+1):
            if text1[i-1] == text2[j-1]:
                print(f'text1[i-1]: text1[{i}-1] text2[j-1]: text2[{j}-1]')
                dp[i][j] = dp[i-1][j-1] + 1
                print(dp)
            else:
                #print(f'dp[i-1][j] : dp[{i}-1][{j}] dp[i][j-1]: dp[{i}][{j}-1]')
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    print(dp)
    return dp[m][n]

text1 = "adce"
text2 = "aed"
print(longestCommonSubsequence(text1,text2))

