def align_score(str1, str2, m, n):
    gap=-10
    
    l=['A','R','N','D','C','Q','E','G','H','I','L','K','M','F','P','S','T','W','Y','V' ]
    
    blosum62 = [[4, -1, -2, -2, 0, -1, -1, 0, -2, -1, -1, -1, -1, -2, -1, 1, 0, -3, -2, 0],
            [-1, 5, 0, -2, -3, 1, 0, -2, 0, -3, -2, 2, -1, -3, -2, -1, -1, -3, -2, -3],
            [-2, 0, 6, 1, -3, 0, 0, 0, 1, -3, -3,  0, -2, -3, -2,  1,  0, -4, -2, -3 ],
            [-2, -2,  1,  6, -3,  0,  2, -1, -1, -3, -4, -1, -3, -3, -1,  0, -1, -4, -3, -3],
            [ 0, -3, -3, -3,  9, -3, -4, -3, -3, -1, -1, -3, -1, -2, -3, -1, -1, -2, -2, -1],
            [-1,  1,  0,  0, -3,  5,  2, -2,  0, -3, -2,  1,  0, -3, -1,  0, -1, -2, -1, -2],
            [-1,  0,  0,  2, -4,  2,  5, -2,  0, -3, -3,  1, -2, -3, -1,  0, -1, -3, -2, -2 ],
            [ 0, -2,  0, -1, -3, -2, -2,  6, -2, -4, -4, -2, -3, -3, -2,  0, -2, -2, -3, -3],
            [-2,  0,  1, -1, -3,  0,  0, -2,  8, -3, -3, -1, -2, -1, -2, -1, -2, -2,  2, -3],
            [-1, -3, -3, -3, -1, -3, -3, -4, -3,  4,  2, -3,  1,  0, -3, -2, -1, -3, -1,  3],
            [-1, -2, -3, -4, -1, -2, -3, -4, -3,  2,  4, -2,  2,  0, -3, -2, -1, -2, -1,  1],
            [-1,  2,  0, -1, -3,  1,  1, -2, -1, -3, -2,  5, -1, -3, -1,  0, -1, -3, -2, -2,],
            [-1, -1, -2, -3, -1,  0, -2, -3, -2,  1,  2, -1,  5,  0, -2, -1, -1, -1, -1,  1],
            [-2, -3, -3, -3, -2, -3, -3, -3, -1,  0,  0, -3,  0,  6, -4, -2, -2,  1,  3, -1],
            [-1, -2, -2, -1, -3, -1, -1, -2, -2, -3, -3, -1, -2, -4,  7, -1, -1, -4, -3, -2],
            [1, -1,  1,  0, -1,  0,  0,  0, -1, -2, -2,  0, -1, -2, -1,  4,  1, -3, -2, -2],
            [0, -1,  0, -1, -1, -1, -1, -2, -2, -1, -1, -1, -1 ,-2, -1,  1,  5, -2, -2,  0],
            [-3, -3, -4, -4, -2, -2, -3, -2, -2, -3, -2, -3, -1,  1, -4, -3, -2, 11,  2, -3],
            [-2, -2, -2, -3, -2, -1, -2, -3 , 2, -1, -1, -2, -1,  3, -3, -2, -2,  2,  7, -1],
            [0, -3, -3, -3, -1, -2, -2, -3, -3,  3,  1, -2,  1, -1, -2, -2,  0, -3, -1,  4, -3]
        ]


   
    dp = [[0 for x in range(n + 1)] for x in range(m + 1)] 
  
 
    for i in range(m + 1): 
        for j in range(n + 1): 

            if i == 0: 
                dp[i][j] = j*gap   
            elif j == 0: 
                dp[i][j] = i*gap    
            elif str1[i-1] == str2[j-1]: 
                dp[i][j] = max( dp[i-1][j-1]+blosum62[ l.index( str1[i-1] ) ][  l.index( str2[j-1] ) ], dp[i-1][j]+gap, dp[i][j-1]+gap ) 
  
            elif str1[i-1]!=str2[j-1]: 
                dp[i][j] = max( dp[i-1][j-1]+blosum62[ l.index( str1[i-1] ) ][  l.index( str2[j-1] ) ], dp[i-1][j]+gap, dp[i][j-1]+gap )    
  
    print(dp)
    #return dp[m][n] 

    #row string
    row_string=['*']
    for ele in str1:
        row_string.append(ele)

    #column string
    col_string=["*"]
    for ele in str2:
        col_string.append(ele)
    
    print(row_string)
    print(col_string)

    i,j=m,n
    align_str1=''
    align_str2=''

    while i>0 or j>0:
            if dp[i-1][j-1]>=dp[i-1][j] and dp[i-1][j-1]>=dp[i][j-1]:
                align_str1=align_str1+row_string[i]
                align_str2=align_str2+col_string[j]

                i=i-1
                j=j-1
            
            elif dp[i][j-1]>=dp[i-1][j-1] and dp[i][j-1]>=dp[i-1][j]:
                align_str2=align_str2+col_string[j]
                align_str1=align_str1+'*'

                i=i
                j=j-1

            elif dp[i-1][j]>dp[i-1][j-1] and dp[i-1][j]>dp[i][j-1]:
                align_str1=align_str1+row_string[i]
                align_str2=align_str2+'*'

                i=i-1
                j=j

            
    
    print(align_str1[::-1])
    print(align_str2[::-1])

    return dp[m][n]

str1 = "MLAWSFARYCRAGERVRGKDSKLDQCLAMKQRLRSQTAWVPILGLVFPSCVTLDRAMGLSDGEWQLVLNVWGKVEADIPSHGQEVLIRLFKGHPETLEKFDKFKHLKSEDEMKASEDLKKHGATVLTALGGILKKKGHHEAEIKPLAQSHATKHKIPVKYLEFISECIIQVLQSKHPGDFGADAQGAMNKALELFRKDMASNYKELGFQG"
str2 = "MGLSDGEWQLVLNVWGKVEADIPGHGQEVLIRLFKGHPETLEKFDKFKHLKSEDEMKASEDLKKHGATVLTALGGILKKKGHHEAEIKPLAQSHATKHKIPVKYLQFISECIIQVLQSKHPGDFGADAQGAMNKALELFRKDMASNYKELGFQG"
  
print(align_score(str2, str1, len(str2), len(str1))) 

str1="MLAWSFARYCRAGER"
str2="MGLSDGEW"
print(align_score(str2,str1, len(str2),len(str1)))

