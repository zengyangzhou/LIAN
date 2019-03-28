'''
https://www.nowcoder.com/question/next?pid=6910869&qid=126952&tid=22641318
一个合法的括号匹配序列被定义为:
1. 空串""是合法的括号序列
2. 如果"X"和"Y"是合法的序列,那么"XY"也是一个合法的括号序列
3. 如果"X"是一个合法的序列,那么"(X)"也是一个合法的括号序列
4. 每个合法的括号序列都可以由上面的规则生成
例如"", "()", "()()()", "(()())", "(((()))"都是合法的。
从一个字符串S中移除零个或者多个字符得到的序列称为S的子序列。
例如"abcde"的子序列有"abe","","abcde"等。
定义LCS(S,T)为字符串S和字符串T最长公共子序列的长度,即一个最长的序列W既是S的子序列也是T的子序列的长度。
小易给出一个合法的括号匹配序列s,小易希望你能找出具有以下特征的括号序列t:
1、t跟s不同,但是长度相同
2、t也是一个合法的括号匹配序列
3、LCS(s, t)是满足上述两个条件的t中最大的
因为这样的t可能存在多个,小易需要你计算出满足条件的t有多少个。

如样例所示: s = "(())()",跟字符串s长度相同的合法括号匹配序列有:
"()(())", "((()))", "()()()", "(()())",其中LCS( "(())()", "()(())" )为4,其他三个都为5,所以输出3.

输入描述:
输入包括字符串s(4 ≤ |s| ≤ 50,|s|表示字符串长度),保证s是一个合法的括号匹配序列。

输出描述:
输出一个正整数,满足条件的t的个数。

输入例子1:
(())()

输出例子1:
3

'''

import sys
from itertools import combinations, permutations


def get_len_lcs(a):
    b = list(a)
    c = list(permutations(a, len(a)))

    lcs_re = []
    all_sen = []
    for sen in c:
        sen = list(sen)
        if sen not in all_sen:
            #print('sen', sen)
            all_sen.append(sen)
            for i in range(len(sen)):
                # c = list(b[i])
                #print(c)
                lens = len(sen)
                loc_left = [ind for ind, val in enumerate(sen) if val == '(']
                loc_right = [ind for ind, val in enumerate(sen) if val == ')']
                for i in range(len(loc_left)):
                    if loc_right[i] > loc_left[i]:
                        lens = lens - 2
            if lens == 0:
                #print('sen use', sen)
                LCS_mat = [[0 for i in range(len(b) + 1)] for i in range(len(sen) + 1)]
                for row_num in range(len(b)):
                    for col_num in range(len(sen)):

                        if b[row_num] != sen[col_num]:
                            LCS_mat[row_num + 1][col_num + 1] = max(LCS_mat[row_num][col_num + 1],
                                                                    LCS_mat[row_num + 1][col_num])

                        if b[row_num] == sen[col_num]:
                            LCS_mat[row_num + 1][col_num + 1] = LCS_mat[row_num][col_num] + 1

                lcs_re.append(max(max(LCS_mat)))
    lcs_re = sorted(lcs_re[1:])
    print(lcs_re)
    len_lcs = lcs_re.count(lcs_re[-1])
    print(len_lcs)

a = '(())()'
get_len_lcs(a)

'''
50%通过， 内存超限
import sys
from itertools import combinations, permutations


def get_len_lcs(a):
    a = a.strip()
    b = list(a)
    #print(b)
    c = list(permutations(a, len(a)))

    lcs_re = []
    all_sen = []
    for sen in c:
        sen = list(sen)
        if sen not in all_sen:
            #print('sen', sen)
            all_sen.append(sen)
            for i in range(len(sen)):
                # c = list(b[i])
                #print(c)
                lens = len(sen)
                loc_left = [ind for ind, val in enumerate(sen) if val == '(']
                loc_right = [ind for ind, val in enumerate(sen) if val == ')']
                for i in range(len(loc_left)):
                    if loc_right[i] > loc_left[i]:
                        lens = lens - 2
            if lens == 0:
                #print('sen use', sen)
                LCS_mat = [[0 for i in range(len(b) + 1)] for i in range(len(sen) + 1)]
                for row_num in range(len(b)):
                    for col_num in range(len(sen)):

                        if b[row_num] != sen[col_num]:
                            LCS_mat[row_num + 1][col_num + 1] = max(LCS_mat[row_num][col_num + 1],
                                                                    LCS_mat[row_num + 1][col_num])

                        if b[row_num] == sen[col_num]:
                            LCS_mat[row_num + 1][col_num + 1] = LCS_mat[row_num][col_num] + 1

                lcs_re.append(max(max(LCS_mat)))
    lcs_re = sorted(lcs_re[1:])
    #print(lcs_re)
    len_lcs = lcs_re.count(lcs_re[-1])
    print(len_lcs)
for a in sys.stdin:
    #print(type(a))
    get_len_lcs(a)
'''
