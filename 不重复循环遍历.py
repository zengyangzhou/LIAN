#注意后面的index是怎么变化的
nums = ['a','b','c','d']
for ind1,ele1 in enumerate(nums):

    for ind2,ele2 in enumerate(nums[ind1+1:-1]):
        for ind3,ele3 in enumerate(nums[ind2+ind1+2:]):
            #print(ind1,ind1+,ind3)
            print(ele1,ele2,ele3)
