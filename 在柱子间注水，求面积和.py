"""
给定一个直方图(也称柱状图)，假设有人从上面源源不断地倒水，最后直方图能存多少水量?直方图的宽度为 1。



上面是由数组 [0,1,0,2,1,0,1,3,2,1,2,1] 表示的直方图，在这种情况下，可以接 6 个单位的水（蓝色部分表示水）。 感谢 Marcos 贡献此图。

示例:

输入: [0,1,0,2,1,0,1,3,2,1,2,1]
输出: 6

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/volume-of-histogram-lcci
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

"""
class Solution:
    def trap(self, height: List[int]) -> int:
        lens = len(height)
        if lens < 3:
            return 0
        highest = max(height)
        height_reverse = height[::-1]
        #print(height_reverse)
        area = 0
        i_water = 0
        for i in range(1, highest+1):

            for ind1, ele1 in enumerate(height):
                if ele1 >= i:
                    ind_left = ind1
                    break
            for ind2, ele2 in enumerate(height_reverse):
                #print('---', ele2, ind2)
                if ele2 >= i:

                    ind_right = lens - (ind2 + 1)
                    break
            if ind_right - 1 > ind_left:
                #print(ind_right, ind_left)
                area += 1*(ind_right-ind_left+1)
                i_water = i

            else:

                break
            #print(i, area)
        area_alr = 0
        for ele in height:
            if ele <= i_water:
                area_alr += ele
            else:
                area_alr += i_water

        return area-area_alr
