#这个网站写得很详细   https://www.cnblogs.com/Meanwey/p/9741334.html


import re
pattern_num = re.compile(r'\d+')
pattern_symb = re.compile(r'\D+')
str = '1+2*33-4/5*3+4/2'  #66.2
num_lst = pattern_num.findall(str)
symb_lst = pattern_symb.findall(str)
# print(num_lst)
# print(symb_lst)

def symple_cal(eq): #计算普通加减乘除计算，不包括有括号情况
    import re
    pattern_num = re.compile(r'\d+\.?\d+|\d+')
    pattern_symb = re.compile(r'[+*/-]')

    num_lst = list(map(float, pattern_num.findall(eq)))
    symb_lst = pattern_symb.findall(eq)
    print(num_lst,symb_lst)
    if len(num_lst) - len(symb_lst) == 1:
        while True:
            for ind,symb in enumerate(symb_lst):
                if symb == '*':
                    res_rec = num_lst[ind] * num_lst[ind+1]
                    num_lst[ind] = res_rec
                    num_lst.pop(ind+1)
                    symb_lst.pop(ind)
                    break
                elif symb == '/':
                    res_rec = num_lst[ind] / num_lst[ind + 1]
                    num_lst[ind] = res_rec
                    num_lst.pop(ind+1)
                    symb_lst.pop(ind)
                    break
            #print(num_lst)
            if '*' not in symb_lst and '/' not in symb_lst:
                break
        # print(num_lst)
        # print(symb_lst)
        while True:
            for ind, symb in enumerate(symb_lst):
                if symb == '+':
                    res_rec = num_lst[ind] + num_lst[ind + 1]
                    num_lst[ind] = res_rec
                    num_lst.pop(ind + 1)
                    symb_lst.pop(ind)
                    break
                elif symb == '-':
                    res_rec = num_lst[ind] - num_lst[ind + 1]
                    num_lst[ind] = res_rec
                    num_lst.pop(ind + 1)
                    symb_lst.pop(ind)
                    break
            # print(num_lst)
            if '+' not in symb_lst and '-' not in symb_lst:
                break


        print(num_lst)

symple_cal('1+2*33.5-4/5*3+4/122')
print(1+2*33.5-4/5*3+4/122)
print(eval('1+(2*33.5-4/5*3)+4/122'))
# a = '123+32.21-2333*0.6/2+23'
# print(re.findall('\d+\.?\d+|\d+',a))    #\.  这个点就是字符为‘.’的意思，可以更改为其他字符
# print(re.findall('[+*/-]',a))
