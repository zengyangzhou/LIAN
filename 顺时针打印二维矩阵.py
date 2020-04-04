a = [[1,2,3,4]]*6

#顺时针打印2维矩阵
def circle_pri(a):
    row_num = len(a)
    col_num = len(a[0])
    xs = 0
    ys = 0
    xsmall_lim = -1
    xbig_lim = row_num
    ysamll_lim = -1
    ybig_lim = col_num
    count = 0
    pri_rec_lst = []
    while True:
        #right
        for i in range(row_num):
            if [xs, ys] not in pri_rec_lst:
                print(a[xs][ys])
                count += 1
                pri_rec_lst.append([xs, ys])
            ys += 1
            if ys == ybig_lim:
                xsmall_lim+=1
                ys-=1
                break
        if count >= row_num * col_num:
            break
        print('---')
        #print(xs,ys)
        # down
        for i in range(row_num):
            if [xs, ys] not in pri_rec_lst:
                print(a[xs][ys])
                count += 1
                pri_rec_lst.append([xs, ys])
            xs += 1
            if xs == xbig_lim:
                ybig_lim-=1
                xs-=1
                break
        if count >= row_num * col_num:
            break
        print('----')
        # left
        for i in range(row_num):
            if [xs, ys] not in pri_rec_lst:
                print(a[xs][ys])
                count += 1
                pri_rec_lst.append([xs, ys])
            ys -= 1
            if ys == ysamll_lim:
                xbig_lim-=1
                ys+=1
                break
        if count >= row_num * col_num:
            break
        print('---')

        # up
        for i in range(row_num):
            if [xs, ys] not in pri_rec_lst:
                print(a[xs][ys])
                count += 1
                pri_rec_lst.append([xs, ys])
            xs -= 1
            if xs == xsmall_lim:
                ysamll_lim+=1
                xs+=1
                break
        if count >= row_num * col_num:
            break
        print('---')

circle_pri(a)
