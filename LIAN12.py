import sys
import copy

def cal_adj_sub(a_list):
    sub = 0
    if len(a_list) == 1:
        #print('0')
        return 0
    for i in range(len(a_list)):
        sub += abs(a_list[i] - a_list[i+1])

        if i == len(a_list) - 2:
            break
    #print(sub)
    return sub

def get_most_index(a_list, m):
    b_list = copy.deepcopy(a_list)
    temp = []
    for i in range(m):
        temp.append(b_list.index(max(b_list)))
        b_list[b_list.index(max(b_list))] = min(b_list)
    temp.sort()
    return temp

def sing_ez(lens, a):
    # b = copy.deepcopy(a)
    min_dif = 1000

    org = copy.deepcopy(a)
    for i in range(lens+1):
        max_list = []
        a = copy.deepcopy(org)
        b = copy.deepcopy(a)
        if i != lens:
            ind = get_most_index(a, i)

            #print('ind', ind)
            # print(i)
            #print(ind)

            for n in ind:
                max_list.append(a[n])
                b.remove(a[n])
            #print(max_list, b)
            diff1 = cal_adj_sub(max_list)
            diff2 = cal_adj_sub(b)
            if diff1 + diff2 < min_dif:
                min_dif = diff1 + diff2
        else:
            min_dif2 = cal_adj_sub(a)


    print(min(min_dif, min_dif2))
i = 0
for line in sys.stdin:
    i = i + 1
    if i == 1:
        lens = int(line)
    else:
        line = line.strip().split()
        a = list(map(int, line))
sing_ez(lens, a)
