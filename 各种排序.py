a_list = [4, 5, 6, 7, 3, 2, 6, 9, 8]
# 1.冒泡排序：它重复地走访过要排序的数列，一次比较两个元素，如果他们的顺序错误就把他们交换过来。走访数列的工作是重复地进行直到没有再需要交换，也就是说该数列已经排序完成
# 时间复杂度：O(n²)
# 空间复杂度：O(1)
# 稳定性：稳定

def bubble_sort(blist):
    count = len(blist)
    for i in range(0, count):
        for j in range(i + 1, count):
            if blist[i] > blist[j]:
                blist[i], blist[j] = blist[j], blist[i]
    return blist


blist = bubble_sort(a_list)
#print(blist)

#选择排序（Selection sort）是一种简单直观的排序算法。它的工作原理如下。首先在未排序序列中找到最小（大）元素，存放到排序序列的起始位置，然后，
#再从剩余未排序元素中继续寻找最小（大）元素，然后放到已排序序列的末尾。以此类推，直到所有元素均排序完毕。
def select_sort(alist):
    """
    选择排序
    :param alist:
    :return:
    """
    n = len(alist)
    for j in range(n-1):
        min_index = j
        for i in range(j + 1, n):
            if alist[min_index] > alist[i]:
                min_index = i
        if min_index != j:
            alist[j], alist[min_index] = alist[min_index], alist[j]
    print(a_list)
#select_sort(a_list)



#插入排序：不断从未排序的序列选择数字加入到有序序列中，切在有序序列中找到合适的位置
def insert_sort(alist):
    """
    选择排序
    :param alist:
    :return:
    """
    n = len(alist)
    for j in range(1, n):
        i = j
        while i > 0:
            if alist[i] < alist[i-1]:
                alist[i], alist[i-1] = alist[i-1], alist[i]
                i -= 1
            else:
                break
    print('insert_sort:', a_list)
insert_sort(a_list)

#快速排序：快速排序（英语：Quicksort），又称划分交换排序（partition-exchange sort），通过一趟排序将要排序的数据分割成独立的两部分，
# 其中一部分的所有数据都比另外一部分的所有数据都要小，然后再按此方法对这两部分数据分别进行快速排序，
# 整个排序过程可以递归进行，以此达到整个数据变成有序序列。
a_list = [4, 5, 6, 7, 3, 2, 6, 9, 8]
def quick_sort(alist, start, end):
    """
    快速排序
    :param alist:
    :return:
    """
    # n = len(alist)
    if start >= end:
        print('quick_sort:', a_list)
        return a_list
    mid = alist[start]
    low = start
    high = end

    while low < high:
        # 这里用alist[high] >= mid 而不是alist[high]>mid是为了把所有和中间值相等的都移动到一遍，而不是移来移去
        while low < high and alist[high] >= mid:
            high -= 1
        alist[low] = alist[high]
        while low < high and alist[low] < mid:
            low += 1
        alist[high] = alist[low]
    alist[low] = mid
    quick_sort(alist, start, low)
    quick_sort(alist, low+1, end)
    #print('quick_sort:', a_list)

res = quick_sort(a_list,0,len(a_list)-1)

#归并排序是采用分治法的一个非常典型的应用。归并排序的思想就是先递归分解数组，再合并数组。
#将数组分解最小之后，然后合并两个有序数组，基本思路是比较两个数组的最前面的数，
#谁小就先取谁，取了后相应的指针就往后移一位。然后再比较，直至一个数组为空，最后把另一个数组的剩余部分复制过来即可。
a_list = [4, 5, 6, 7, 3, 2, 6, 9, 8]
def merge_sort(alist):
    n = len(alist)
    if n <= 1:
        return alist
    # 分为两部分,对每部分进行排序
    mid = n // 2

    # 假设这已经是排序好的了
    left = merge_sort(alist[0:mid])
    right = merge_sort(alist[mid:])

    # 对排序好的进行合并
    left_index = 0
    right_index = 0
    result = []
    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            result.append(left[left_index])
            left_index += 1
        else:
            result.append(right[right_index])
            right_index += 1
    # 如果左边先走到尽头，则把右边剩余所有加进来；如果右边先走到尽头，则把左边剩余所有加进来
    # 最终第一层的result把left 和 right 的result 都包含进来了
    result += left[left_index:]
    result += right[right_index:]
    return result
res = merge_sort(a_list)
print('merge_sort:', res)
