#交换列表中两个元素位置
def swap(ind1, ind2, a_list):
    a = a_list[ind1]
    b = a_list[ind2]
    a_list[ind1] = b
    a_list[ind2] = a
    return a_list

#生成一个大根堆
def big_root_heap(a_list):
    for i, ele in enumerate(a_list):
        father_ind = int((i - 1) / 2)
        while True:
            if a_list[i] > a_list[father_ind]:
                a_list = swap(i, father_ind, a_list)
            i = father_ind
            #print(father_ind)
            #print(a_list)
            if (i - 1) / 2 < 0:
                break
            father_ind = int((i - 1) / 2)
    #print(a_list)
    return a_list

#生成一个小根堆
def small_root_heap(a_list):
    for i, ele in enumerate(a_list):
        father_ind = int((i - 1) / 2)
        while True:
            if a_list[i] < a_list[father_ind]:
                a_list = swap(i, father_ind, a_list)
            i = father_ind
            #print(father_ind)
            #print(a_list)
            if (i - 1) / 2 < 0:
                break
            father_ind = int((i - 1) / 2)
    #print(a_list)
    return a_list



#堆中的一个值改变了，重新排序使得堆还是大根堆
def heapify(ind, val, heap):
    #print('ind', ind)
    if val > heap[ind]: #值变大

        heap[ind] = val
        father_ind = (ind - 1) / 2
        if father_ind < 0:
            return heap
        else:
            father_ind = int(father_ind)
            while True:

                if heap[ind] > heap[father_ind]:
                    heap = swap(ind, father_ind, heap)
                ind = father_ind
                father_ind = (ind - 1) / 2
                if father_ind < 0:
                    break
                father_ind = int(father_ind)
            return heap
    elif val == heap[ind]: #值不变
        return heap

    else: #值变小
        if ind == len(heap) - 1:
            return heap
        else: #值改变的位置不再堆最后
            heap[ind] = val
            sonl_ind = 2 * ind + 1
            if sonl_ind < len(heap) - 1: # 它的左孩子不是堆最后一个
                sonr_ind = sonl_ind + 1
                while True:
                    if heap[ind] < heap[sonl_ind] or heap[ind] < heap[sonr_ind]:
                        #print(ind, sonl_ind, sonr_ind)
                        if heap[sonl_ind] > heap[sonr_ind]:
                            heap = swap(ind, sonl_ind, heap)
                            ind = sonl_ind
                        else:
                            heap = swap(ind, sonr_ind, heap)
                            ind = sonr_ind
                        sonl_ind = 2 * ind + 1
                        #print(sonl_ind)
                        #print('1')
                        if sonl_ind < len(heap) - 1:
                            sonr_ind = sonl_ind + 1
                        else:
                            #return heap
                            break
                    else:
                        break
            else: #没有叶子或者只有一个左叶子
                try:
                    if heap[sonl_ind] > val:
                        heap = swap(sonl_ind, ind, heap)
                        return heap
                except:
                    return heap
            return heap

# 堆中去掉堆顶，使得它还是大根堆
def heaprm_top(heap):
    bot_val = heap[-1]
    # heap = swap(0, -1, heap)
    heap.pop(-1)
    heap = heapify(0, bot_val, heap)
    return heap

# 堆排序,排列为从小到大的数列
def heap_order(heap):
    order_list = []
    lens = len(heap)
    for i in range(lens-1):
        order_list.append(heap[0])
        heap = heaprm_top(heap)
        #print(heap)
    order_list.append(heap[0])
    order_list2 = order_list[::-1]
    return order_list2
